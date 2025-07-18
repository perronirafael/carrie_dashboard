
from django.urls import path
from .views import DashboardView, FilteredChartDataView, MissedCheckinsChartView, PatientStatusDataView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('chart-data/', FilteredChartDataView.as_view(), name='chart-data'),
    path('missed-checkins-data/', MissedCheckinsChartView.as_view(), name='missed-checkins-data'),
    path('patient-status-data/', PatientStatusDataView.as_view(), name='patient_status_data'),
]
