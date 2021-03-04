from rest_framework import serializers
from .models import ServiceModel, LogModel, StatisticsModel


class ServiceSerializer(serializers.ModelSerializer):
    """
    serializer for service model
    """
    class Meta:
        model = ServiceModel
        fields = ('id', 'name', 'status', 'interface', 'available_interfaces')


class ServiceUpdateStatusSerializer(serializers.ModelSerializer):
    """
    serializer for service status updating
    """
    class Meta:
        model = ServiceModel
        fields = ('status', )


class ServiceUpdateInterfaceSerializer(serializers.ModelSerializer):
    """
    serializer for service interface updating
    """
    class Meta:
        model = ServiceModel
        fields = ('interface', )


class ServiceUpdateInterfacesSerializer(serializers.ModelSerializer):
    """
    serializer for service interfaces list updating
    """
    class Meta:
        model = ServiceModel
        fields = ('available_interfaces', )


class ServiceRenameSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = ServiceModel
        fields = ('name', )


class LogSerializer(serializers.ModelSerializer):
    """
    serializer for log model
    """
    class Meta:
        model = LogModel
        fields = ('id', 'log_data', 'service', 'date_time')


class StatisticsSerializer(serializers.ModelSerializer):
    """
    serializer for statistics model
    """
    class Meta:
        model = StatisticsModel
        fields = ('id', 'statistics', 'service', 'date_time')
