from django.contrib import admin

from account.models import (
    User,
    PTeachingUser,
    SupportTeachingUser,
    Address,
)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    empty_value_display = '---'
    list_display = [
        'first_name',
        'last_name',
        'middle_name',
        'email',
        'phone',
    ]
    list_display_links = [
        'email',
        'phone',
    ]
    filter_horizontal = [
        'groups',
        'user_permissions',
    ]
    list_filter = [
        'groups',
        'education_level',
        'stake',
    ]
    autocomplete_fields = [
        'registration_address',
        'resident_address',
    ]


class RelatedUserMixin:

    @admin.display(ordering="user__first_name", description="First name")
    def get_first_name(self, obj: PTeachingUser):
        return obj.user.first_name


@admin.register(PTeachingUser)
class PTSAdmin(admin.ModelAdmin, RelatedUserMixin):
    empty_values_display = '---'
    list_display = [
        'get_first_name',
    ]


@admin.register(SupportTeachingUser)
class STSAdmin(admin.ModelAdmin):
    empty_values_display = '---'


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    empty_values_display = '---'
    search_fields = [
        "country__name",
        "region__name",
        "city__name",
    ]
