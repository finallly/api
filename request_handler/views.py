from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from .models import ServiceModel, LogModel
from .serializers import ServiceSerializer, ServiceUpdateStatusSerializer, LogSerializer, \
    ServiceUpdateInterfaceSerializer


class ServiceView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """
    view for actions on Service model CRUD
    """

    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]


class ServiceStatusView(mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    """
    view for updating service status C
    """

    queryset = ServiceModel.objects.all()
    serializer_class = ServiceUpdateStatusSerializer
    permission_classes = [IsAuthenticated]


class ServiceInterfaceView(mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    """
    view for updating service interface C
    """

    queryset = ServiceModel.objects.all()
    serializer_class = ServiceUpdateInterfaceSerializer
    permission_classes = [IsAuthenticated]


class ServiceInterfacesView(mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """
    view for updating service interfaces list C
    """

    queryset = ServiceModel.objects.all()
    serializer_class = ServiceUpdateInterfaceSerializer
    permission_classes = [IsAuthenticated]


class LogView(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              viewsets.GenericViewSet):
    """
    view for actions of Log CR
    """

    queryset = LogModel.objects.all()
    serializer_class = LogSerializer
    permission_classes = [IsAuthenticated]
