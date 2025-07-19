from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse
from django.db.models import Count
from patients.models import Patient, SessionAdherenceResult, PatientSession, Diagnosis
from django.db.models.functions import TruncDate
from datetime import datetime, timedelta

from django.views import View
from django.http import JsonResponse

class DashboardView(TemplateView):
    template_name = "dashboard.html"


class PatientStatusDataView(View):
    def get(self, request):
        diagnosis = request.GET.get("diagnosis")
        age_group = request.GET.get("age")
        start = request.GET.get("start")
        end = request.GET.get("end")

        patient_qs = Patient.objects.all()

        if diagnosis and diagnosis != "all":
            try:
                diagnosis_obj = Diagnosis.objects.get(name=diagnosis)
                patient_qs = patient_qs.filter(diagnosis=diagnosis_obj)
            except Diagnosis.DoesNotExist:
                return JsonResponse({"status_counts": [], "alert_count": 0})

        if age_group and age_group != "all":
            if age_group == "young":
                patient_qs = patient_qs.filter(age__gte=18, age__lte=30)
            elif age_group == "mid":
                patient_qs = patient_qs.filter(age__gte=31, age__lte=50)
            elif age_group == "older":
                patient_qs = patient_qs.filter(age__gte=51)

        if start:
            start_date = datetime.strptime(start, "%Y-%m-%d").date()
            patient_qs = patient_qs.filter(last_session_date__gte=start_date)
        if end:
            end_date = datetime.strptime(end, "%Y-%m-%d").date()
            patient_qs = patient_qs.filter(last_session_date__lte=end_date)

        status_counts = (
            patient_qs
            .values("status")
            .annotate(total=Count("id"))
            .order_by("total")
        )

        alert_count = patient_qs.filter(status="Potential Emergency Reported").count()

        return JsonResponse({
            "status_counts": list(status_counts),
            "alert_count": alert_count
        })


class FilteredChartDataView(View):
    def get(self, request):
        diagnosis = request.GET.get("diagnosis")
        age_group = request.GET.get("age")
        start = request.GET.get("start")
        end = request.GET.get("end")

        session_qs = PatientSession.objects.all()
        patient_qs = Patient.objects.all()

        if diagnosis and diagnosis != "all":
            try:
                diagnosis_obj = Diagnosis.objects.get(name=diagnosis)
                patient_qs = patient_qs.filter(diagnosis=diagnosis_obj)
            except Diagnosis.DoesNotExist:
                return JsonResponse({"error": f"Diagnosis '{diagnosis}' not found"}, status=400)

        if age_group and age_group != "all":
            if age_group == "young":
                patient_qs = patient_qs.filter(age__gte=18, age__lte=30)
            elif age_group == "mid":
                patient_qs = patient_qs.filter(age__gte=31, age__lte=50)
            elif age_group == "older":
                patient_qs = patient_qs.filter(age__gte=51)

        patient_ids = patient_qs.values_list("id", flat=True)
        session_qs = session_qs.filter(patient_id__in=patient_ids)

        if start:
            start_date = datetime.strptime(start, "%Y-%m-%d").date()
            session_qs = session_qs.filter(session_date__gte=start_date)
            

        if end:
            end_date = datetime.strptime(end, "%Y-%m-%d").date()
            session_qs = session_qs.filter(session_date__lte=end_date)

        session_ids = session_qs.values_list("id", flat=True)
        adherence_qs = SessionAdherenceResult.objects.filter(session_id__in=session_ids)

        def agg(field):
            return list(
                adherence_qs.values(field)
                .annotate(total=Count("id"))
                .order_by(field)
            )

        return JsonResponse({
            "medication": agg("medication"),
            "diet": agg("diet"),
            "exercise": agg("exercise"),
        })

class MissedCheckinsChartView(View):
    def get(self, request):
        diagnosis = request.GET.get("diagnosis")
        age_group = request.GET.get("age")
        start = request.GET.get("start")
        end = request.GET.get("end")

        session_qs = PatientSession.objects.filter(status="Missed Check")
        patient_qs = Patient.objects.all()

        if diagnosis and diagnosis != "all":
            try:
                diagnosis_obj = Diagnosis.objects.get(name=diagnosis)
                patient_qs = patient_qs.filter(diagnosis=diagnosis_obj)
            except Diagnosis.DoesNotExist:
                return JsonResponse({"error": f"Diagnosis '{diagnosis}' not found"}, status=400)

        if age_group and age_group != "all":
            if age_group == "young":
                patient_qs = patient_qs.filter(age__gte=18, age__lte=30)
            elif age_group == "mid":
                patient_qs = patient_qs.filter(age__gte=31, age__lte=50)
            elif age_group == "older":
                patient_qs = patient_qs.filter(age__gte=51)

        patient_ids = patient_qs.values_list("id", flat=True)
        session_qs = session_qs.filter(patient_id__in=patient_ids)

        if start:
            start_date = datetime.strptime(start, "%Y-%m-%d").date()
            session_qs = session_qs.filter(session_date__gte=start_date)
        if end:
            end_date = datetime.strptime(end, "%Y-%m-%d").date()
            session_qs = session_qs.filter(session_date__lte=end_date)

        data = session_qs.values("session_date").annotate(total=Count("id")).order_by("session_date")

        response = [
            {"day": item["session_date"].isoformat(), "total": item["total"]}
            for item in data
        ]

        return JsonResponse(response, safe=False)

