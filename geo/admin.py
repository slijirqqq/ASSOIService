from django.contrib import admin

from geo.models import (
    Region, City, Country
)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass
