from django.contrib import admin
from .models import (
    CheckerUser, GetInfoInspector, UpdateInspector, FoundClientByInspector)
from rangefilter.filters import DateRangeFilterBuilder


@admin.register(CheckerUser)
class ModelNameAdmin(admin.ModelAdmin):
    """Admin view for CheckerUser model."""
    list_display = [
        "username", "uid", "getinfo_points", "update_points",
        "foundclient_points", "total_points"]
    search_fields = ["uid", "username"]
    list_filter = ["username", "uid"]

    def getinfo_points(self, obj: CheckerUser) -> int:
        """Represents points to '/getinfo actions.'"""
        return obj.info.count()

    def update_points(self, obj: CheckerUser) -> int:
        """Represents points to successfull '/update actions.'"""
        return obj.updates.count()

    def foundclient_points(self, obj: CheckerUser) -> int:
        """Represents points to successfull client found by inspector.'"""
        return obj.clients.count()

    def total_points(self, obj: CheckerUser) -> int:
        """Total points for all useful actions."""
        return (
                self.getinfo_points(obj) + self.update_points(obj)
                + self.foundclient_points(obj)
        )


@admin.register(GetInfoInspector)
class ModelNameAdmin(admin.ModelAdmin):
    """Admin view for GetInfoInspector model."""
    list_display = ["user", "created_at"]
    search_fields = ["user__username"]
    list_filter = [
        "user__username",
        ("created_at", DateRangeFilterBuilder())
    ]


@admin.register(UpdateInspector)
class ModelNameAdmin(admin.ModelAdmin):
    """Admin view for UpdateInspector model."""
    list_display = ["user", "created_at"]
    search_fields = ["user__username"]
    list_filter = [
        "user__username",
        ("created_at", DateRangeFilterBuilder())
    ]


@admin.register(FoundClientByInspector)
class FoundClientByInspectorAdmin(admin.ModelAdmin):
    """Admin view for FoundClientByInspector model."""
    list_display = ["user", "created_at"]
    search_fields = ["user__username", ("created_at",)]
    list_filter = [
        "user__username",
        ("created_at", DateRangeFilterBuilder())
    ]
