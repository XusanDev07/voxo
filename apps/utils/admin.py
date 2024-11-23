from django.contrib import admin

from apps.utils.models.regions import Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass
