# In your_app/urls.py
from django.urls import path
from . import views
from .views import (
    ServiceUpdateView,
confirmed_receptions_for_trainer,
    ReceptionView,
    annual_report, DoctorDetailView,
    MakeAppointmentView,
CheckUserView,
    export_to_word_by_date,
ServiceListView,
    ServiceDetailView,
    ServiceCreateView,
    ReceptionListView,
MedicalEquipmentListView, equipment_detail,
diagnosis_and_treatment_plan,
DoctorsListView, ServicesListView, ServiceListViewAPI,
TrainingEquipmentsListView, MasseursListView,
confirmed_and_arrived_receptions)

app_name = 'main'

urlpatterns = [
    path('', ReceptionView.as_view(), name='list_doctors'),
    path('services/update/<int:pk>/', ServiceUpdateView.as_view(), name='service_update'),
    path('services/', ServiceListView.as_view(), name='service_list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('services/create/', ServiceCreateView.as_view(), name='service_create'),
    path('receptions/', ReceptionListView.as_view(), name='reception_list'),
    path('reception/<int:reception_id>/diagnosis_and_treatment_plan/',
         diagnosis_and_treatment_plan, name='diagnosis_and_treatment_plan'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('annual-report/', annual_report, name='annual_report'),
    path('reception-confirmation/', views.reception_confirmation_view, name='reception_confirmation'),
    path('export_to_excel/', views.export_to_excel, name='export_to_excel'),
    path('export_to_word/<str:date>/', export_to_word_by_date, name='export_to_word_by_date'),
    path('receptions/unconfirmed/', views.unconfirmed_receptions_list, name='unconfirmed_receptions_list'),
    path('receptions/add/', views.add_reception, name='add_reception'),
    path('receptions/<int:pk>/delete/', views.delete_reception, name='delete_reception'),
    path('receptions/<int:pk>/', views.reception_detail, name='reception_detail'),
    path('receptions_detail/<int:pk>/', views.view_reception_detail, name='reception_detail_for_doctor'),
    path('medical-equipment/', MedicalEquipmentListView.as_view(), name='medical_equipment_list'),
    path('medical-equipment/<int:pk>/', equipment_detail, name='equipment_detail'),
    path('confirmed_arrived/', confirmed_and_arrived_receptions, name='confirmed-and-arrived-receptions'),
    path('trainer_receptions/', confirmed_receptions_for_trainer, name='confirmed-receptions-for-trainer'),

    path('api/make_appointment', MakeAppointmentView.as_view(), name='make_appointment'),
    path('api/check_user', CheckUserView.as_view(), name='check_user'),
    path('api/doctors', DoctorsListView.as_view(), name='doctors-list'),
    path('api/services_api', ServiceListViewAPI.as_view(), name='services-list-api'),
    path('api/services', views.ServiceListViewAPI.as_view(), name='services-list-api'),
    path('api/masseur', MasseursListView.as_view(), name='masseur-list'),
    path('api/training', TrainingEquipmentsListView.as_view(), name='training-list'),
    path('download_word_report/', views.download_word_report, name='download_word_report'),

]
