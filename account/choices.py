from django.db import models
from django.utils.translation import gettext_lazy as _


class UserStaffChoices(models.TextChoices):
    admin = "admin", _("Admin")
    p_teaching = "pts", _("PTS")
    s_teaching = "sts", _("STS")
    aspirant = "aspirant", _("Aspirant")
    student = "student", _("Student")


class EducationLevelChoices(models.TextChoices):
    high_education = "high_education", _("High education")
    college_tech_education = "college_tech_education", _("College tech education")
    college_education = "college_education", _("College education")


class StakeChoices(models.TextChoices):
    full_time = "staff", _("Staff")
    internal_part_time = "internal", _("Internal part-time worker")
    external_part_time = "external", _("External part-time worker")


class PTeachingChoices(models.TextChoices):
    assistant = "assistant", _("Assistant")
    high_teacher = "high_teacher", _("High teacher")
    docent = "docent", _("Docent")
    professor = "professor", _("Professor")


class SupportChoices(models.TextChoices):
    engineer = "engineer", _("Engineer")
    high_engineer = "high_engineer", _("High engineer")
    lead_engineer = "lead_engineer", _("Lead engineer")
    first_category_technician = "first_category_technician", _("Laboratory assistant of the 1st category")
    laboratory_head = "laboratory_head", _("Head laboratory")
    first_category_technic = "first_category_technic", _("Technician 1st category")
