from django.db import models
from django.utils.translation import gettext_lazy as _


class AcademicDegreeChoices(models.TextChoices):
    technic_phd = "technic_phd", _("Technic PhD")
    chemistry_phd = "chemistry_phd", _("Chemistry PhD")
    candidate_of_pedagogical_sciences = "candidate_of_pedagogical_sciences", _("Pedagogical PhD")
    candidate_of_physical_mathematical_sciences = "candidate_of_physical_mathematical_sciences", \
                                                  _("Physical and Mathematical PhD")
    doctor_of_technical_sciences = "doctor_of_technical_sciences", _("Doctor of Technical Sciences")
    doctor_of_chemistry_sciences = "doctor_of_chemistry_sciences", _("Doctor of Chemistry Sciences")
    doctor_of_pedagogical_sciences = "doctor_of_pedagogical_sciences", _("Doctor of Pedagogical Sciences")
    doctor_og_physic_and_math_sciences = "doctor_og_physic_and_math_sciences", \
                                         _("Doctor of Physical and Mathematical Sciences")


class AcademicTitleChoices(models.TextChoices):
    professor = "professor", _("Professor")
    docent = "docent", _("Docent")
    scientist = "scientist", _("Scientist employee")
    high_scientist = "high_scientist", _("High scientist employee")
