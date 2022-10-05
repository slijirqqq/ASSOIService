from django.db import models
from django.utils.translation import gettext_lazy as _

from academic.choices import AcademicDegreeChoices, AcademicTitleChoices
from app_core.models import BaseModel


class AcademicBase(BaseModel):
    date = models.DateField(verbose_name=_("Date"))
    diploma_number = models.CharField(verbose_name=_("Diploma number"), max_length=13)

    class Meta:
        abstract = True
        ordering = ("id",)


class AcademicDegree(AcademicBase):
    name = models.CharField(max_length=128, verbose_name=_("Academic degree"), choices=AcademicDegreeChoices.choices)

    class Meta:
        verbose_name = _("Academic degree")
        verbose_name_plural = _("Academic degrees")


class AcademicTitle(AcademicBase):
    name = models.CharField(max_length=128, verbose_name=_("Academic title"), choices=AcademicTitleChoices.choices)

    class Meta:
        verbose_name = _("Academic title")
        verbose_name_plural = _("Academic titles")
