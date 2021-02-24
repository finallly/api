from django.db import models


class StatusModel(models.Model):
    status = models.CharField(max_length=10)


class InterfaceModel(models.Model):
    service = models.ForeignKey(StatusModel, on_delete=models.CASCADE, primary_key=True)
    interface = models.CharField(max_length=100)


class DataModel(models.Model):
    service = models.ForeignKey(StatusModel, on_delete=models.CASCADE, primary_key=True)
    data = models.JSONField()


class LogModel(models.Model):
    service = models.ForeignKey(StatusModel, on_delete=models.CASCADE, primary_key=True)
    log_data = models.JSONField()
