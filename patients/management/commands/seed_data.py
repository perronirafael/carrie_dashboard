from django.core.management.base import BaseCommand
from patients.models import Provider, Diagnosis, Patient, PatientSession, SessionAlert, SessionAdherenceResult
from django.utils import timezone
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Seed initial data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        SessionAdherenceResult.objects.all().delete()
        SessionAlert.objects.all().delete()
        PatientSession.objects.all().delete()
        Patient.objects.all().delete()
        Diagnosis.objects.all().delete()
        Provider.objects.all().delete()

        providers = ['Dr. Smith', 'Dr. Jones', 'Dr. Lee', 'Dr. Brown', 'Dr. Garcia']
        for name in providers:
            Provider.objects.get_or_create(name=name)

        diagnoses = [
            'CHF Stage I',
            'CHF Stage II',
            'CHF Stage III',
            'CHF Stage IV',
            'Diabetes',
            'Hypertension'
        ]
        for name in diagnoses:
            Diagnosis.objects.get_or_create(name=name)

        patients_list = []
        for i in range(10):
            patient = Patient.objects.create(
                first_name=f'First{i}',
                last_name=f'Last{i}',
                mrn=f'MRN{i:03d}',
                provider=Provider.objects.order_by('?').first(),
                diagnosis=Diagnosis.objects.order_by('?').first(),
                status=random.choice([
                    'Stable',
                    'Clinical Concern',
                    'Potential Emergency Reported'
                ]),
                last_session_date=timezone.now() - timedelta(
                days=random.randint(0, 30),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59)
            ),
                notifications=random.randint(0, 5),
                age=random.randint(18, 90),
            )
            patients_list.append(patient)

        alert_types = ['High BP', 'Missed Check']
        for patient in patients_list:
            for _ in range(5):
                session = PatientSession.objects.create(
                    patient=patient,
                    session_date=timezone.now().date() - timedelta(days=random.randint(0, 30)),
                    status=random.choice([
                        'Missed Check',
                        'Awnsered',
                    ])
                )
                SessionAlert.objects.create(
                    patient=patient,
                    alert_type=random.choice(alert_types)
                )
                SessionAdherenceResult.objects.create(
                    session=session,
                    medication=random.choice(['Adherant', 'Non-adherant', 'Partial']),
                    diet=random.choice(['Adherant', 'Non-adherant', 'Needs improvement']),
                    exercise=random.choice(['Regular exercise', 'No exercise', 'Occasional exercise']),
                )

        self.stdout.write(self.style.SUCCESS('Seed data loaded'))
