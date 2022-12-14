from __future__ import annotations

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from account.choices import (
    StakeChoices,
    SupportChoices,
    PTeachingChoices,
    EducationLevelChoices,
)
from app_core.models import BaseModel


class UserManager(BaseUserManager):

    def _create_user(self, email: str, password: str, **extra_fields):
        """
        :param phone: phone number of user
        :param password: password of user
        :param extra_fields: another fields that defined in User model
        :return: User object
        """
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not password:
            raise ValueError('The given password must be set for superuser')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email=email, password=password, **extra_fields)


class Address(BaseModel):
    country = models.OneToOneField("geo.Country", on_delete=models.CASCADE, verbose_name=_("Country"))
    region = models.OneToOneField("geo.Region", on_delete=models.CASCADE, verbose_name=_("Region"), db_index=True)
    city = models.OneToOneField("geo.City", on_delete=models.CASCADE, verbose_name=_("City"), db_index=True)
    street = models.CharField(_('Street'), max_length=256)
    house = models.CharField(_('House'), max_length=256)

    def __str__(self):
        return f'{self.country.name}, {self.region.name}, ??.{self.city.name}, ????.{self.street}, ??.{self.house}'

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Address")
        ordering = ['region__name']
        db_table = "Address"


class User(AbstractBaseUser, PermissionsMixin):
    # Personal and system user info
    email = models.EmailField(db_index=True, verbose_name=_('Email'), max_length=256, unique=True)
    phone = PhoneNumberField(max_length=14, verbose_name=_("Phone number"), db_index=True, blank=True, null=True,
                             unique=True)
    first_name = models.CharField(verbose_name=_('First name'), max_length=128, db_index=True)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=128, db_index=True)

    # Only personal user info
    middle_name = models.CharField(verbose_name=_('Middle name'), max_length=128, blank=True, null=True, db_index=True)
    photo = models.ImageField(verbose_name=_('Avatar'), upload_to='media/images', blank=True)
    birth_date = models.DateField(verbose_name=_('Birth date'), blank=True, null=True)
    education_level = models.CharField(_('Education level'), choices=EducationLevelChoices.choices,
                                       blank=True, null=True, max_length=128, db_index=True)
    stake = models.CharField(_('Stake'), choices=StakeChoices.choices, blank=True, null=True, max_length=128)
    registration_address = models.ForeignKey("Address", verbose_name=_('Registration address'), null=True,
                                             on_delete=models.CASCADE, related_name='registered_users', blank=True)
    resident_address = models.ForeignKey("Address", verbose_name=_('Resident address'), on_delete=models.CASCADE,
                                         related_name='resident_users', blank=True, null=True)
    total_work_experience = models.PositiveSmallIntegerField(_("Total work experience"), blank=True, null=True)

    # Only system user info
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["id", "first_name", "last_name"]
        db_table = "User"

    def __str__(self):
        return f"{self.__class__.__name__} - {self.id}: {self.last_name} {self.first_name} {self.middle_name}"


class ProfessionalDevelopment(BaseModel):
    date = models.DateField(_('Date of advanced training'))
    position = models.CharField(_('Place of advanced training'), max_length=256)
    hours_count = models.PositiveSmallIntegerField(_('Number of hours'))

    class Meta:
        verbose_name = _("Professional Development")
        verbose_name_plural = _("Professional Development")
        ordering = ["date"]
        db_table = "ProfessionalDevelopment"

    def __str__(self):
        return f"""
        {self.__class__.__name__} - {self.id}: 
        Completed In {self.position} on {self.date} in {self.hours_count} hours"""


class PTeachingUser(BaseModel):
    # External user info
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('User'), on_delete=models.CASCADE,
                                related_name='pts_users', db_index=True)
    # Education user info
    academic_degree = models.ForeignKey("academic.AcademicDegree", verbose_name=_('Academic degree'),
                                        on_delete=models.CASCADE, blank=True, null=True)
    academic_title = models.ForeignKey("academic.AcademicTitle", verbose_name=_('Academic title'),
                                       on_delete=models.CASCADE, blank=True, null=True)

    # Teaching user info
    post = models.CharField(_('Post'), choices=PTeachingChoices.choices, max_length=128, blank=True, null=True)
    total_teaching_experience = models.PositiveSmallIntegerField(_('Total teaching experience'), blank=True, null=True)
    contract_term = models.PositiveSmallIntegerField(_('Contract term'), blank=True, null=True)
    start_term = models.DateField(_('Start term'), blank=True, null=True)
    end_term = models.DateField(_('End term'), blank=True, null=True)
    part_of_stake = models.DecimalField(_('Part of stake'), decimal_places=2, max_digits=5, null=True,
                                        validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True)
    professional_development = models.ForeignKey("ProfessionalDevelopment", verbose_name=_('Professional development'),
                                                 on_delete=models.CASCADE, blank=True, null=True, related_name='users')

    class Meta:
        verbose_name = _("PTS")
        verbose_name_plural = _("PTS employee")
        db_table = "PTS"

    def __str__(self):
        return f"""
        {self.__class__.__name__} - {self.id}: 
        {self.user.last_name} {self.user.first_name} {self.user.middle_name}"""


class SupportTeachingUser(BaseModel):
    # External user info
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('std_user'), on_delete=models.CASCADE,
                                related_name='sts_users', db_index=True)
    # Support user info
    post = models.CharField(_('Post'), choices=SupportChoices.choices, max_length=128)

    class Meta:
        verbose_name = _("STS")
        verbose_name_plural = _("STS employee")
        db_table = "STS"

    def __str__(self):
        return f"""
        {self.__class__.__name__} - {self.id}: 
        {self.user.last_name} {self.user.first_name} {self.user.middle_name}"""
