from rest_framework.generics import ListAPIView, RetrieveAPIView

from property.models import Property
from property.serializers import PropertySerializer


class PropertyAPIList(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyAPIDetail(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer