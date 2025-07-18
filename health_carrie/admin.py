from django.contrib import admin
from .models import Provider, Diagnosis, Patient, PatientSession, SessionAlert, SessionAdherenceResult

admin.site.register(Provider)
admin.site.register(Diagnosis)
admin.site.register(Patient)
admin.site.register(PatientSession)
admin.site.register(SessionAlert)
admin.site.register(SessionAdherenceResult)
