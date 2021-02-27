from rest_framework import serializers
from .models import ServiceModel


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceModel
        fields = ('id', 'name', 'status', 'interface', 'available_interfaces')
