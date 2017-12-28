from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
import json
from shop.models import *
from dblab2.settings import DB, DB_CONNECTION
import psycopg2
import psycopg2.extras
from django.utils import timezone

class Home(View):
    def get(self, request):
        if request.GET.__contains__('to') and request.GET.__contains__('from'):
            analyzes = Analysis.objects.filter(created_gte=request.GET['from'], created_lte=request.GET['to'])
        elif request.GET.__contains__('notcontains'):
            analyzes = Analysis.objects.exclude(type__name__contains=request.GET['notcontains'])
        else:
            analyzes = Analysis.objects.all()
        analyzes = [{
            "patient_name": analysis.patient.first_name + " " + analysis.patient.last_name,
            "doctor_name": analysis.doctor.first_name + " " + analysis.doctor.last_name,
            "assistant_name": analysis.lab_assistant.first_name + " " + analysis.lab_assistant.last_name,
            "patient_id": analysis.patient.id,
            "doctor_id": analysis.doctor.id,
            "assistant_id": analysis.lab_assistant.id,
            "type": analysis.type.name,
            "type_id": analysis.type.id,
            "value": analysis.value,
            "id": analysis.id,
            "modified": analysis.modified,
        } for analysis in analyzes]

        patients = Patient.objects.all()
        doctors = Doctor.objects.all()
        assistans = LabAssistant.objects.all()
        types = AnalysisType.objects.all()
        return render(request, "home.html", {"analyzes": analyzes,
                                             "patients": patients,
                                             "doctors": doctors,
                                             "assistans": assistans,
                                             "types": types})

    def post(self, request):
        analysis = Analysis.objects.get(id=int(request.POST['id']))
        analysis.patient = int(request.POST['patient'])
        analysis.doctor = int(request.POST['doctor'])
        analysis.lab_assistant = int(request.POST['assistant'])
        analysis.type = int(request.POST['type'])
        analysis.value = float(request.POST['value'])
        analysis.modified = timezone.now()
        analysis.save()
        return self.get(request)


class Delete(View):
    def get(self, request):
        if request.GET.__contains__("id"):
            Analysis.objects.delete(id=request.GET['id'])
        return redirect('/')


class Create(View):
    def post(self, request):
        DB.execute("""
            INSERT INTO shop_analysis (
                created, 
                modified, 
                value, 
                doctor_id,
                lab_assistant_id,
                patient_id,
                type_id)
            VALUES (
                (now()), 
                (now()), 
                (%s),
                (%s),
                (%s),
                (%s),
                (%s));
            """, (float(request.POST['value']),
                  int(request.POST['doctor']),
                  int(request.POST['assistant']),
                  int(request.POST['patient']),
                  int(request.POST['type'])))
        DB_CONNECTION.commit()
        Analysis.objects.create(value=request.POST['value'],
                                doctor=request.POST['doctor'],
                                lab_assistant=request.POST['assistant'],
                                type=request.POST['type'],
                                patient=request.POST['patient'])
        return redirect('/')
