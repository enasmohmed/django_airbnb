from django.urls import path

from .api_view import PropertyAPIList, PropertyAPIDetail
from .views import PropertyList, PropertyDetail

app_name = 'property'

urlpatterns = [
    path('', PropertyList.as_view(), name='property_list'),
    path('<slug:slug>', PropertyDetail.as_view(), name='property_detail'),

    # api
    path('api/list', PropertyAPIList.as_view(), name='property_api_list'),
    path('api/list/<int:pk>', PropertyAPIDetail.as_view(), name='property_api_detail'),
]
