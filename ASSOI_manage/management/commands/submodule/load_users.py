import abc
import json
import logging
from pathlib import Path
from typing import Dict, Optional, List, AnyStr, Set, Union

from django.contrib.auth import get_user_model, models
from django.contrib.auth.hashers import make_password
from django.db.models import QuerySet

from ASSOI_manage.management.commands.submodule import SUBMODULE_DIR
from account.choices import UserStaffChoices
from account.models import User

logger = logging.getLogger(__name__)


class UsersLoader:

    def __init__(self):
        self.__users_file: Path = SUBMODULE_DIR / "user.json"
        self.__groups: List[AnyStr] = UserStaffChoices.values
        self.__user_data: Optional[Dict] = None

    def load(self):
        logging.info("Start to init accounts data...")
        self.__user_data = self.load_users()

        groups_init = GroupInit(self.groups)
        groups = groups_init.init()

        users_init = UserInit(self.user_data, groups)
        _ = users_init.init()

        logger.info("...Accounts data inited")

    def load_users(self) -> Dict:
        logger.info("Start to upload user data...")
        with open(self.__users_file, "r", encoding="utf-8") as user_file:
            data = json.load(user_file)
        logger.info("...User data uploaded")
        return data

    @property
    def user_data(self) -> Dict:
        if self.__user_data is None:
            raise NotImplementedError("Please loading user data")
        return self.__user_data

    @property
    def groups(self) -> List[AnyStr]:
        return self.__groups


class AbstractInit(abc.ABC):
    object_model: Union[User, models.Group] = None

    def __init__(self, data: List[AnyStr]):
        if self.object_model is None:
            raise NotImplementedError("Please define object model to creating")
        self.data = data

    def init(self):
        logger.info(f"Start to init {self.object_model.__name__}.")

        exists_instances = self.get_exists_instances()

        logger.info(f"Exists {len(exists_instances)} {self.object_model.__name__} objects.")

        not_exists_instances = self.get_not_exists_instances(self.data, exists_instances)

        to_create = []
        for object_key in not_exists_instances:
            to_create.append(
                self.fill_to_create(
                    object_key,
                )
            )

        created = self.object_model.objects.bulk_create(to_create)

        logger.info(f"Created {len(to_create)} {self.object_model.__name__} objects.")

        result = created + list(exists_instances)

        self.work_with_related(result)

        logger.info(f"{self.object_model.__name__} objects inited.")

        return result

    def get_exists_instances(self):
        return self.object_model.objects.filter(
            **self.get_filter(self.data)
        )

    def get_not_exists_instances(self, data: List[AnyStr], instances: QuerySet) -> Set[AnyStr]:
        return set(
            data
        ).difference(
            instances.values_list(
                self.lookup,
                flat=True
            )
        )

    @abc.abstractmethod
    def work_with_related(self, instances):
        ...

    @abc.abstractmethod
    def fill_to_create(self, object_key: AnyStr) -> Union[User, models.Group]:
        ...

    @staticmethod
    @abc.abstractmethod
    def get_filter(filtering_objects: List[AnyStr]) -> Dict:
        ...

    @property
    @abc.abstractmethod
    def lookup(self):
        ...


class UserInit(AbstractInit):
    object_model = get_user_model()

    def __init__(self, user_data: Dict, groups: List[models.Group]):
        super().__init__(self.__get_usernames(user_data))
        self.__user_data = user_data
        self.__related_data = {}
        self.__groups = groups

    def work_with_related(self, instances: List[User]) -> None:
        for instance in instances:
            if self.__related_data.get(instance.email):
                instance.groups.set(self.__related_data[instance.email])

    @staticmethod
    def __get_usernames(user_data) -> List[AnyStr]:
        usernames = []
        for _, value in user_data.items():
            usernames.append(
                value.get("email")
            )
        return usernames

    def fill_to_create(self, object_key: AnyStr) -> Union[User, models.Group]:
        user_reference: AnyStr = object_key.split("@")[0]
        user_data: Dict = self.__user_data[user_reference]
        self.__related_data[object_key]: List[AnyStr] = [
            group for group in self.__groups if group.name in self.__user_data[user_reference]["email"]
        ]
        user_data["password"] = make_password(user_data["password"])
        user_data.pop("groups")
        return self.object_model(
            **user_data
        )

    @staticmethod
    def get_filter(filtering_objects: List[AnyStr]) -> Dict:
        return {
            "email__in": filtering_objects,
        }

    @property
    def lookup(self):
        return 'email'


class GroupInit(AbstractInit):
    object_model = models.Group

    def work_with_related(self, instances) -> None:
        return

    def fill_to_create(self, object_key: AnyStr) -> Union[User, models.Group]:
        return self.object_model(
            name=object_key
        )

    @staticmethod
    def get_filter(filtering_objects: List[AnyStr]) -> Dict:
        return {
            "name__in": filtering_objects
        }

    @property
    def lookup(self):
        return 'name'
