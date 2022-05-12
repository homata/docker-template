from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# from .models import TrafficFlow, Annotation
#
#
# class TrafficFlowResource(resources.ModelResource):
#     class Meta:
#         model = TrafficFlow
#         # exclude = ("created_at", "updated_at")
#         fields = ("serialnumber", "device_id", "smartphone_id", "physical_device_id", "app_version", "timestamp", "lat", "lon", "created_at", "updated_at")
#
#
# class TrafficFlowModelAdmin(ImportExportModelAdmin):
#     resource_class = TrafficFlowResource
#     ordering = ["-pk"]
#     # exclude = ("created_at", "updated_at")
#     list_display = ("pk", "serialnumber", "device_id", "smartphone_id", "physical_device_id", "app_version", "timestamp", "lat", "lon")
#     list_display_links = ("serialnumber", "device_id", "smartphone_id")
#     search_fields = ["serialnumber"]
#     list_per_page = 50
#
#
# admin.site.register(TrafficFlow, TrafficFlowModelAdmin)
