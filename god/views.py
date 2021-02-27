from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema

from .models import ServiceModel
from .serializers import ServiceSerializer


class CreateServiceView(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

