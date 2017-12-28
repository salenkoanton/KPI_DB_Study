from django.db import models
from django.utils import timezone


class Patient(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class Doctor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    profession = models.CharField(max_length=64)


class LabAssistant(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class AnalysisType(models.Model):
    name = models.CharField(max_length=64)


class Analysis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    lab_assistant = models.ForeignKey(LabAssistant, on_delete=models.PROTECT)
    type = models.ForeignKey(AnalysisType, on_delete=models.PROTECT)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    value = models.FloatField(default=0.0)
