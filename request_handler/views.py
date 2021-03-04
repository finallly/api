from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import ServiceModel, LogModel, StatisticsModel
from .serializers import ServiceSerializer, ServiceUpdateStatusSerializer, LogSerializer, \
    ServiceUpdateInterfaceSerializer, ServiceUpdateInterfacesSerializer, StatisticsSerializer, ServiceRenameSerializer


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
    view for updating service status U
    """

    queryset = ServiceModel.objects.all()
    serializer_class = ServiceUpdateStatusSerializer
    permission_classes = [IsAuthenticated]


class ServiceInterfaceView(mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    """
    view for updating service interface U
    """

    queryset = ServiceModel.objects.all()
    serializer_class = ServiceUpdateInterfaceSerializer
    permission_classes = [IsAuthenticated]


class ServiceInterfacesView(mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    """
    view for updating service interfaces list U
    """

    queryset = ServiceModel.objects.all()
    serializer_class = ServiceUpdateInterfacesSerializer
    permission_classes = [IsAuthenticated]


class ServiceRenameView(mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    """
    view for renaming a service U
    """

    queryset = ServiceModel.objects.all()
    serializer_class = ServiceRenameSerializer
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
    permission_classes = [IsAuthenticatedOrReadOnly]


class StatisticsView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    view for actions of statistics model CR
    """

    queryset = StatisticsModel.objects.all()
    serializer_class = StatisticsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
