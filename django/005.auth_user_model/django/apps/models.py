from django.db import models
# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point
from django.utils import timezone
# from django.utils.translation import ugettext as _

import logging
logger = logging.getLogger(__file__)
# logger = logging.getLogger('app')

#
# class TrafficFlow(models.Model):
#
#     class Meta:
#         verbose_name = _('TrafficFlow')
#         verbose_name_plural = _('TrafficFlows')
#
#     serialnumber = models.CharField(_('serialnumber'), max_length=256, blank=True, null=True, default=None)
#     device_id = models.CharField(_('deviceID'), max_length=256, blank=True, null=True, default=None)
#     smartphone_id = models.CharField(_('smartphone_id'), max_length=256, blank=True, null=True, default=None)
#     physical_device_id = models.CharField(_('physical_device_id'), max_length=256, blank=True, null=True, default=None)
#
#     app_version = models.CharField(_('app version'), max_length=128, blank=True, null=True, default=None)
#     timestamp = models.DateTimeField(_('timestamp'), blank=True, null=True)
#
#     lat = models.FloatField(_('latitude'), default=0.0, null=False)
#     lon = models.FloatField(_('longitude'), default=0.0, null=False)
#
#     # geom = models.GeometryField(_('geom'), srid=4326, null=True, blank=True)
#     # point = models.PointField(_('point'), srid=4326, null=True, blank=True, default=None)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
#
#     def __str__(self):
#         return "TrafficFlow ID: " + self.smartphone_id + ": " + self.device_id + ": " + str(self.pk)
#
#
# class Annotation(models.Model):
#     class Meta:
#         verbose_name = _('Annotation')
#         verbose_name_plural = _('Annotations')
#
#     # TrafficFlow
#     # traffic_flow = models.ForeignKey(TrafficFlow, verbose_name='TrafficFlow', related_name='annotation', null=True, on_delete=models.SET_NULL)
#     traffic_flow_id = models.IntegerField(_('traffic_flow_id'), blank=False, null=False, default=0)
#
#     lat = models.FloatField(_('longitude'), default=0.0, null=False)
#     lon = models.FloatField(_('latitude'), default=0.0, null=False)
#     bearing = models.FloatField(_('bearing'), default=0.0, null=False)
#
#     distance = models.FloatField(_('distance'), default=0.0, null=False)
#     angle = models.FloatField(_('angle'), default=0.0, null=False)
#
#     class_name = models.CharField('class', max_length=128, blank=True, null=True, default=None)
#     orientation = models.CharField('orientation', max_length=128, blank=True, null=True, default=None)
#
#     # geom = models.GeometryField(_('geom'), srid=4326, null=True, blank=True)
#     # point = models.PointField(_('point'), srid=4326, null=True, blank=True, default=None)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
#
#     def __str__(self):
#         return "Annotation ID: " + str(self.pk)
