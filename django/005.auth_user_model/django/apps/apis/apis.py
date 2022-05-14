from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

import os
import traceback
from datetime import datetime
import json

import logging
logger = logging.getLogger(__file__)

# from .serializers import TrafficFlowSerializer, AnnotationSerializer
#
#
# class TrafficFlowAPIView(APIView):
#     """
#     TrafficFlow API
#
#     Notes
#     -----
#     URL: http://127.0.0.1:8000/api/v1.0/traffic_flow/
#
#     See Also
#     --------
#     * Try #036 – DjangoでJWT認証のAPIを構築してみた: https://day-journal.com/memo/try-036/
#     """
#
#     # API パーミッション
#     # permission_classes = (AllowAny,)
#     # permission_classes = [IsAuthenticated]
#     authentication_classes = (TokenAuthentication, )
#
#     def get(self, request, *args, **keywords):
#         result = {}
#         try:
#             response = Response(result, status=status.HTTP_200_OK)
#
#         except Exception as e:
#             traceback.print_exc()
#             response = Response(result, status=status.HTTP_404_NOT_FOUND)
#
#         return response
#
#     def post(self, request, **keywords):
#         try:
#             body_data = request.body
#             body_data_str = body_data.decode("utf-8")
#             post_data = json.loads(body_data_str)
#
#             self.save(post_data)
#             return Response({"code": status.HTTP_200_OK, "message": "ok"}, status=status.HTTP_200_OK)
#
#         except Exception as e:
#             traceback.print_exc()
#             return Response({"code": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": "Internal Server Error"},
#                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#     def save(self, post_data):
#         data = {
#             "serialnumber": post_data["serialnumber"],
#             "device_id":  post_data["deviceID"],
#             "smartphone_id":  post_data["smartphone_id"],
#             "physical_device_id":  post_data["physical_device_id"],
#             "app_version":  post_data["app_version"],
#             "timestamp":  post_data["timestamp"],
#             "lat":  post_data["location"]["lat"],
#             "lon":  post_data["location"]["lon"]
#         }
#         serializer = TrafficFlowSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         traffic_flow = serializer.save()
#
#         annotation_objects = post_data["annotation"]["objects"]
#         for annotation_object in annotation_objects:
#             data = {
#                 "traffic_flow_id": traffic_flow.pk,
#                 "lat": annotation_object["location"]["lat"],
#                 "lon": annotation_object["location"]["lon"],
#                 "bearing": annotation_object["location"]["bearing"],
#                 "distance": annotation_object["distance"],
#                 "angle": annotation_object["angle"],
#                 "class_name": annotation_object["class"],
#                 "orientation": annotation_object["orientation"]
#             }
#             serializer = AnnotationSerializer(data=data)
#             serializer.is_valid(raise_exception=True)
#             annotation = serializer.save()
