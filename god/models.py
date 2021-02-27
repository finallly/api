from django.db import models


class ServiceModel(models.Model):
    status = models.CharField(max_length=10)
    interface = models.CharField(max_length=100)


class AvailableInterfacesModel(models.Model):
    interfaces = models.JSONField()
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)


class DataModel(models.Model):
    data = models.JSONField()
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)


class LogModel(models.Model):
    log_data = models.JSONField()
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
