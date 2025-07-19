# patients/forms.py
from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('Stable', 'Stable'),
        ('Clinical Concern', 'Clinical Concern'),
        ('Potential Emergency Reported', 'Potential Emergency Reported'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'mrn', 'age',
            'provider', 'diagnosis', 'status',
            'last_session_date'
        ]
        widgets = {
           'last_session_date': forms.DateTimeInput(
               attrs={'type': 'datetime-local'},
               format='%Y-%m-%dT%H:%M',
           ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fld in self.fields.values():
            fld.required = True
            fld.widget.attrs.update({'required': 'required'})

        self.fields['last_session_date'].input_formats = ['%Y-%m-%dT%H:%M']

        if self.instance and getattr(self.instance, 'last_session_date', None):
            dt = self.instance.last_session_date.strftime('%Y-%m-%dT%H:%M')
            self.fields['last_session_date'].initial = dt
