from __future__ import annotations

import abc
import csv
import logging
import time
from copy import copy
from pathlib import Path
from typing import Dict, Optional, List, Set, AnyStr, Tuple

from django.db import models

from geo.models import Geo, Region, City, Country

logger = logging.getLogger(__name__)
SUBMODULE_DIR = Path(__file__).resolve(strict=True).parent


class CadastralLoader:
    __field_names = ['city', 'district_type', 'region_id', 'region', 'region_type']

    def __init__(self):
        self.__file = SUBMODULE_DIR / 'cities.csv'
        self.prepare_data: Optional[Dict] = None
        self.region_uploader = RegionUploader()
        self.cities_uploader = CityUploader(bulk=False)

    def load(self):
        start = time.time()
        with open(self.file_path, 'r') as cadastral_file:
            cadastral_reader = csv.DictReader(cadastral_file, fieldnames=self.__field_names, delimiter=",")
            self.prepare_data = self.__prepare_cadastral_data(cadastral_reader)

        logger.info("Data uploaded")

        country, _ = Country.active_objects.get_or_create(country='RU', defaults={'name': 'Russia'})

        regions = list(self.prepare_data.keys())

        created, exists = self.region_uploader.upload(regions, country)

        logger.info(f"Created {len(created)} regions and exists {len(exists)}")

        regions = created + list(exists)

        to_create_cities = []
        exists_cities = []
        for region in regions:
            to_create, exists = self.cities_uploader.upload(self.prepare_data[region.name], region)
            to_create_cities.extend(to_create)
            exists_cities.extend(list(exists))

        created = City.active_objects.bulk_create(to_create_cities)

        logger.info(f"Created {len(created)} cities and exists {len(exists_cities)}")

        end = time.time()

        logger.info(f"Data upload for {end - start} seconds")

    @staticmethod
    def __prepare_cadastral_data(reader: csv.DictReader) -> Dict:
        prepare_data = {}
        for cadastral_data in reader:
            city, region = cadastral_data['city'], cadastral_data['region']
            if region not in prepare_data:
                prepare_data[region] = [city]
            elif city not in prepare_data[region]:
                prepare_data[region].append(city)
            else:
                continue
        return prepare_data

    @property
    def file_path(self):
        return self.__file


class CadastralUploader(abc.ABC):
    model_to_upload = None

    def __init__(self, bulk: bool = True):
        self.__bulk = bulk
        if self.model_to_upload is None:
            raise NotImplementedError("Please define model to upload data")
        if not issubclass(self.model_to_upload, Geo):
            raise TypeError(f"{self.model_to_upload} is not subclass of {Geo}")

    def upload(self, data: List[AnyStr], related_object: Geo) -> Tuple[List[Geo], models.QuerySet[Geo]]:
        exists_instances = self.__get_exists_instances(data)
        not_exists_instances = self.__get_not_exists_instances(data, exists_instances)

        to_create = []
        for cadastral_name in not_exists_instances:
            to_create.append(
                self.create(cadastral_name, related_object)
            )

        if self.__bulk:
            created = self.model_to_upload.active_objects.bulk_create(to_create)
        else:
            created = to_create

        return copy(created), copy(exists_instances)

    @abc.abstractmethod
    def create(self, name: AnyStr, related_object: Geo) -> Geo:
        ...

    def __get_exists_instances(self, data: List[AnyStr]) -> models.QuerySet:
        instances = self.model_to_upload.active_objects.filter(
            name__in=data,
        )
        return instances

    @staticmethod
    def __get_not_exists_instances(data: List[AnyStr], instances: models.QuerySet) -> Set:
        names = instances.values_list('name', flat=True)
        return set(
            data
        ).difference(
            set(names)
        )


class RegionUploader(CadastralUploader):
    model_to_upload = Region

    def create(self, name: AnyStr, related_object: Geo) -> Region:
        return self.model_to_upload(
            name=name,
            country=related_object,
        )


class CityUploader(CadastralUploader):
    model_to_upload = City

    def create(self, name: AnyStr, related_object: Geo) -> City:
        return self.model_to_upload(
            name=name,
            region=related_object,
        )
