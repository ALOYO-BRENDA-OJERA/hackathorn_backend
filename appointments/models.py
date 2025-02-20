from django.db import models

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient_name} - {self.appointment_date}'
