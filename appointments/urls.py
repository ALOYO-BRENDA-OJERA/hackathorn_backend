from django.urls import path
from .views import AppointmentListCreate, AppointmentDetail

urlpatterns = [
    path('', AppointmentListCreate.as_view(), name='appointment-list-create'),  # Matches /appointments/
    path('<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),  # Matches /appointments/<id>/
]
