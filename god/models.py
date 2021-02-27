from django.db import models


class ServiceModel(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    interface = models.CharField(max_length=100)
    available_interfaces = models.JSONField()


class LogModel(models.Model):
    log_data = models.JSONField()
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
