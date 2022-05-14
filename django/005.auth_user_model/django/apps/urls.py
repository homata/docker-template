from django.urls import path
from . import views
from . import apis

# アプリケーションの名前空間
app_name = 'apps'

urlpatterns = [
    path('', views.index, name='index'),

    # path('api/v1.0/location/', apis.TrafficFlowAPIView.as_view(), name='traffic_flow_api'),
]

