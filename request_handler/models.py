from django.db import models


class ServiceModel(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    active_interface = models.CharField(max_length=100)
    available_interfaces = models.JSONField()

    def __str__(self):
        return self.name


class LogModel(models.Model):
    date_time = models.DateTimeField()
    log_data = models.JSONField()
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)


class StatisticsModel(models.Model):
    date_time = models.DateTimeField()
    statistics = models.JSONField()
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
