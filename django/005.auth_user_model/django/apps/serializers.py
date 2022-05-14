from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

# from .models import TrafficFlow, Annotation
#
#
# class TrafficFlowSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = TrafficFlow
#         fields = ('serialnumber', 'device_id', 'smartphone_id', 'physical_device_id',
#                   'app_version', 'timestamp',  'lat', 'lon')
#
#     serialnumber = serializers.CharField(required=False)
#     device_id = serializers.CharField(required=False)
#     smartphone_id = serializers.CharField(required=False)
#     physical_device_id = serializers.CharField(required=False)
#
#     app_version = serializers.CharField(required=False)
#     timestamp = serializers.DateTimeField()
#
#     lon = serializers.FloatField()
#     lat = serializers.FloatField()
#
#
# class AnnotationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Annotation
#         fields = ('traffic_flow_id', 'lat', 'lon', 'bearing', 'distance', 'angle',
#                   'class_name', 'orientation')
#
#     # traffic_flow = serializers.PrimaryKeyRelatedField(queryset=TrafficFlow.objects.all(), write_only=True)
#     traffic_flow_id = serializers.IntegerField()
#     # lon = SerializerMethodField()
#     # lat = SerializerMethodField()
#     # bearing = SerializerMethodField()
#     lon = serializers.FloatField()
#     lat = serializers.FloatField()
#     bearing = serializers.FloatField()
#
#     distance = serializers.FloatField()
#     angle = serializers.FloatField()
#
#     class_name = serializers.CharField(required=False)
#     orientation = serializers.CharField(required=False)
#
#     def get_lat(self, annotation):
#         return annotation.lat
#
#     def get_lon(self, annotation):
#         return annotation.lon
#
#     def get_bearing(self, annotation):
#         return annotation.bearing
