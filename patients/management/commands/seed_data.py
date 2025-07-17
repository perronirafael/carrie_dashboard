from django.core.management.base import BaseCommand
from patients.models import Provider, Diagnosis, Patient, PatientSession, SessionAlert, SessionAdherenceResult
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Seed initial data'

    def handle(self, *args, **options):
        providers = ['Dr. Smith','Dr. Jones','Dr. Lee']
        diagnoses = ['CHF Stage I','CHF Stage II','Diabetes','Hypertension']
        for name in providers:
            Provider.objects.get_or_create(name=name)
        for name in diagnoses:
            Diagnosis.objects.get_or_create(name=name)
        patients_list = []
        for i in range(10):
            p = Patient.objects.create(
                first_name=f'First{i}', last_name=f'Last{i}', mrn=f'MRN{i}',
                provider=Provider.objects.order_by('?').first(),
                diagnosis=Diagnosis.objects.order_by('?').first(),
                status=random.choice(['Active','Inactive']),
                last_session_date=timezone.now().date(), alerts=random.randint(0,3), notifications=random.randint(0,5)
            )
            patients_list.append(p)
        for p in patients_list:
            for j in range(5):
                s = PatientSession.objects.create(patient=p, session_date=timezone.now().date())
                SessionAlert.objects.create(session=s, alert_type=random.choice(['High BP','Missed Check']))
                SessionAdherenceResult.objects.create(session=s, medication=random.choice([True,False]), diet=random.choice([True,False]), exercise=random.choice([True,False]))
        self.stdout.write(self.style.SUCCESS('Seed data loaded'))
