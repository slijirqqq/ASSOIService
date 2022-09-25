from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ActiveManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class BaseModel(models.Model):
    """Base ASSOI model which will be inherited by the following classes."""

    #: created_at - Date and time when object was created.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    #: updated_at - Date and time when object was updated.
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Updated at"))
    #: deleted - Flag indicating deleted model.
    deleted = models.BooleanField(_("Deleted?"), default=False)

    objects = models.Manager()
    active_objects = ActiveManager()

    class Meta:
        abstract = True

    def save_base(
            self,
            raw=False,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.updated_at = timezone.now()
        super(BaseModel, self).save_base()
