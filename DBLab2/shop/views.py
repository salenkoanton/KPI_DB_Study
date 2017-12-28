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
        """analyzes = [{
            "patient": analysis.patient,
            "doctor": analysis.doctor,
            "labAssistant": analysis.labAssistant,
            "type": analysis.type,
            "created": analysis.created,
            "modified": analysis.modified,
            "value": analysis.value
        } for analysis in Analysis.objects.raw("SELECT * from shop_analysis")]
        """
        SELECT_QUERY = """
            SELECT shop_analysis.value as value, 
                shop_patient.last_name as patient_last_name,
                shop_patient.first_name as patient_first_name,
                shop_patient.id as patient_id,
                
                shop_doctor.last_name as doctor_last_name,
                shop_doctor.first_name as doctor_first_name,
                shop_doctor.id as doctor_id,
                
                shop_labassistant.last_name as assistant_last_name,
                shop_labassistant.first_name as assistant_first_name,
                shop_labassistant.id as assistant_id,
                
                shop_analysistype.name as type,
                shop_analysistype.id as type_id,
                
                shop_analysis.value as value,
                shop_analysis.id as id,
                shop_analysis.modified as modified
                
            FROM shop_analysis 
            INNER JOIN shop_patient ON shop_analysis.patient_id = shop_patient.id
            INNER JOIN shop_doctor ON shop_analysis.doctor_id = shop_doctor.id
            INNER JOIN shop_labassistant ON shop_analysis.lab_assistant_id = shop_labassistant.id
            INNER JOIN shop_analysistype ON shop_analysis.type_id = shop_analysistype.id {0};
        """
        if request.GET.__contains__('to') and request.GET.__contains__('to'):
            DB.execute(SELECT_QUERY.format("WHERE shop_analysis.created < (%s) AND shop_analysis.created > (%s)"),
                       (request.GET['to'],
                        request.GET['from']))
        elif request.GET.__contains__('notcontains'):
            DB.execute(SELECT_QUERY.format("WHERE to_tsvector(shop_analysistype.name) @@ to_tsquery('!" + request.GET['notcontains'] + "')"))
        else:
            DB.execute(SELECT_QUERY.format(""))

        analyzes = DB.fetchall()
        analyzes = [{
            "patient_name": analysis["patient_first_name"] + " " + analysis["patient_last_name"],
            "doctor_name": analysis["doctor_first_name"] + " " + analysis["doctor_last_name"],
            "assistant_name": analysis["assistant_first_name"] + " " + analysis["assistant_last_name"],
            "patient_id": analysis["patient_id"],
            "doctor_id": analysis["doctor_id"],
            "assistant_id": analysis["assistant_id"],
            "type": analysis["type"],
            "type_id": analysis["type_id"],
            "value": analysis["value"],
            "id": analysis["id"],
            "modified": analysis["modified"],
        } for analysis in analyzes]

        DB.execute("""SELECT * FROM shop_patient;""")
        patients = DB.fetchall()

        DB.execute("""SELECT * FROM shop_doctor;""")
        doctors = DB.fetchall()

        DB.execute("""SELECT * FROM shop_labassistant;""")
        assistans = DB.fetchall()

        DB.execute("""SELECT * FROM shop_analysistype;""")
        types = DB.fetchall()
        DB_CONNECTION.commit()
        return render(request, "home.html", {"analyzes": analyzes,
                                             "patients": patients,
                                             "doctors": doctors,
                                             "assistans": assistans,
                                             "types": types})

    def post(self, request):
        print(request.POST)
        DB.execute("""
            UPDATE
            shop_analysis
            SET
                patient_id = {0}, 
                doctor_id = {1}, 
                lab_assistant_id = {2}, 
                type_id = {3}, 
                value = {4}, 
                modified = (now())
            WHERE
            shop_analysis.id = {5};
            """.format(request.POST['patient'],
                       request.POST['doctor'],
                       request.POST['assistant'],
                       request.POST['type'],
                       request.POST['value'],
                       request.POST['id']))
        DB_CONNECTION.commit()
        return self.get(request)


class Delete(View):
    def get(self, request):
        if request.GET.__contains__("id"):
            DB.execute("""
                DELETE FROM shop_analysis
                WHERE shop_analysis.id = {0};
                """.format(request.GET['id']))
            DB_CONNECTION.commit()
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
        return redirect('/')
