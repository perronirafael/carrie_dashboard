# patients/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Patient
from .forms import PatientForm

class PatientListView(ListView):
    model = Patient
    template_name = 'patient_list.html'
    context_object_name = 'patients'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = PatientForm()
        return ctx


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient_form.html'      
    success_url = reverse_lazy('patient_list')

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = self.get_form()
            return render(request, 'patients/partials/patient_form_partial.html', {'form': form})
        return super().get(request, *args, **kwargs)


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient_form.html'
    success_url = reverse_lazy('patient_list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = self.get_form()
            return render(request, 'patients/partials/patient_form_partial.html', {'form': form})
        return super().get(request, *args, **kwargs)


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return render(request, 'patients/partials/patient_confirm_delete_partial.html', {})
        return super().get(request, *args, **kwargs)
