# from django.http import HttpResponse
# from rest_framework import generics
# from .models import Appointment
# from .serializers import AppointmentSerializer

# # Simple view to return a welcome message
# def index(request):
#     return HttpResponse("Welcome to the Appointment Scheduling System")

# # API view to handle listing and creating appointments
# class AppointmentListCreate(generics.ListCreateAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer

# # API view to handle retrieving, updating, and deleting a specific appointment
# class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer


from django.http import HttpResponse
from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentSerializer
from .africastalking_service import send_sms

def index(request):
    return HttpResponse("Welcome to the Appointment Scheduling System")

class AppointmentListCreate(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        # Save the appointment
        appointment = serializer.save()

        # Send an SMS notification (example)
        message = f"New appointment scheduled for {appointment.patient_name} on {appointment.appointment_date}."
        send_sms("recipient_phone_number", message)

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
