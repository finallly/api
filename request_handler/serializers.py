from rest_framework import serializers
from .models import ServiceModel, LogModel


class ServiceSerializer(serializers.ModelSerializer):
    """
    serializer for service model
    """
    class Meta:
        model = ServiceModel
        fields = ('id', 'name', 'status', 'interface', 'available_interfaces')


class LogSerializer(serializers.ModelSerializer):
    """
    serializer for log model
    """
    class Meta:
        model = LogModel
        fields = ('id', 'log_data', 'service')


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
