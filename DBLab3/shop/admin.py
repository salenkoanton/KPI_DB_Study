from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AnalysisType)
admin.site.register(Analysis)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(LabAssistant)


