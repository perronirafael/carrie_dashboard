from django.urls import path
from .views import PatientListView, PatientCreateView, PatientUpdateView, PatientDeleteView

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('new/', PatientCreateView.as_view(), name='patient_create'),
    path('<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_update'),
    path('<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
]
