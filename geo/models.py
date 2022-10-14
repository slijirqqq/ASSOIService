from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from app_core.models import BaseModel


class Geo(BaseModel):
    class Meta:
        ordering = ('id',)
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} - {self.id}: {self.name}"


class Country(Geo):
    country = CountryField(unique=True, verbose_name=_("Country"))

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        db_table = "Country"


class Region(Geo):
    country = models.ForeignKey("Country", on_delete=models.CASCADE, verbose_name=_("Country"))

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
        db_table = "Region"


class City(Geo):
    object_type = "city"

    region = models.ForeignKey("Region", on_delete=models.CASCADE, verbose_name=_("Region"))

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
        db_table = "City"
