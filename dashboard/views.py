from django.views.generic import TemplateView
from django.db.models import Count
from patients.models import Patient, SessionAdherenceResult, PatientSession
from django.db.models.functions import TruncDate

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        status_qs = (
            Patient.objects
                   .values('status')
                   .annotate(total=Count('id'))
                   .order_by('total')
        )
        ctx['status_counts'] = list(status_qs)

        ctx['alert_count'] = Patient.objects.filter(
            status='Potential Emergency Reported'
        ).count()

        med_qs = (
            SessionAdherenceResult.objects
                   .values('medication')
                   .annotate(total=Count('id'))
                   .order_by('medication')
        )
        ctx['medication_counts'] = list(med_qs)

        diet_qs = (
            SessionAdherenceResult.objects
                   .values('diet')
                   .annotate(total=Count('id'))
                   .order_by('diet')
        )
        ctx['diet_counts'] = list(diet_qs)

        ex_qs = (
            SessionAdherenceResult.objects
                   .values('exercise')
                   .annotate(total=Count('id'))
                   .order_by('exercise')
        )
        ctx['exercise_counts'] = list(ex_qs)

        missed_checkins_qs = (
            PatientSession.objects
        .filter(status='missed')
        .annotate(day=TruncDate('session_date'))
        .values('day')
        .annotate(total=Count('id'))
        .order_by('day')
        )
        ctx['missed_checkins'] = list(missed_checkins_qs)

        return ctx
