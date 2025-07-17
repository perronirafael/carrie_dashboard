from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name','last_name','mrn','provider','diagnosis','status','last_session_date']
        widgets = {'last_session_date': forms.DateInput(attrs={'type':'date'})}
