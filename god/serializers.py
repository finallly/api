from rest_framework import serializers
from .models import ServiceModel, LogModel


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceModel
        fields = ('id', 'name', 'status', 'interface', 'available_interfaces')


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogModel
        fields = ('id', 'log_data', 'service')
