from django.contrib import admin

from academic.models import AcademicTitle, AcademicDegree


@admin.register(AcademicTitle)
class AcademicTitleAdmin(admin.ModelAdmin):
    pass


@admin.register(AcademicDegree)
class AcademicDegreeAdmin(admin.ModelAdmin):
    pass
