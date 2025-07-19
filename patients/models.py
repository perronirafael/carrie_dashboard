from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Diagnosis(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Patient(models.Model):
    first_name    = models.CharField(max_length=50)
    last_name     = models.CharField(max_length=50)
    mrn           = models.CharField('MRN', max_length=20, unique=True)
    provider      = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    diagnosis     = models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True)
    status        = models.CharField(max_length=60)
    last_session_date = models.DateTimeField(null=True, blank=True)
    notifications = models.IntegerField(default=0)
    age           = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def alerts(self):
        return self.sessionalert_set.count()


class PatientSession(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    session_date = models.DateField()
    status = models.CharField(max_length=60)

class SessionAlert(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=50)

class SessionAdherenceResult(models.Model):
    session = models.ForeignKey(PatientSession, on_delete=models.CASCADE)
    medication = models.CharField(max_length=50)
    diet = models.CharField(max_length=50)
    exercise = models.CharField(max_length=50)
