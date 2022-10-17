from typing import Union, AnyStr

from django.contrib import admin
from django.contrib.auth import get_user_model

from account.models import (
    PTeachingUser,
    SupportTeachingUser,
    Address,
)


class RelatedUserMixin:
    list_display = [
        'get_last_name',
        'get_first_name',
        'get_middle_name',
        'get_phone',
        'get_email',
    ]

    list_display_links = [
        'get_email',
        'get_phone',
    ]

    @admin.display(ordering="user__first_name", description="First name")
    def get_first_name(self, obj: Union[PTeachingUser, SupportTeachingUser]) -> AnyStr:
        return obj.user.first_name

    @admin.display(ordering="user__last_name", description="Last name")
    def get_last_name(self, obj: Union[PTeachingUser, SupportTeachingUser]) -> AnyStr:
        return obj.user.last_name

    @admin.display(ordering="user__middle_name", description="Middle name")
    def get_middle_name(self, obj: Union[PTeachingUser, SupportTeachingUser]) -> AnyStr:
        return obj.user.middle_name

    @admin.display(ordering="user__phone", description="Phone")
    def get_phone(self, obj: Union[PTeachingUser, SupportTeachingUser]) -> AnyStr:
        return obj.user.phone

    @admin.display(ordering="user__email", description="Email")
    def get_email(self, obj: Union[PTeachingUser, SupportTeachingUser]) -> AnyStr:
        return obj.user.email


@admin.register(PTeachingUser)
class PTSAdmin(RelatedUserMixin, admin.ModelAdmin):
    ...


@admin.register(SupportTeachingUser)
class STSAdmin(RelatedUserMixin, admin.ModelAdmin):
    ...


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    search_fields = [
        "country__name",
        "region__name",
        "city__name",
    ]


admin.site.register(get_user_model())
