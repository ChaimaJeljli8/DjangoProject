
from django.db import models

from AccountApp.models import Doctor,Patient

class Appointment(models.Model):
    reason = models.TextField()
    prescription = models.FileField(
        blank=True, #champs optionnel
        upload_to='prescriptions/'
        )
    
    class Status (models.TextChoices):
        PENDING = "Pending", "En attente"
        ACCEPTED = "Confirmed", "Confirmé"
        REJECTED = "Cancelled", "Annulé"
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    # Methode 2 directement sans declaration de la classe
    # status = models.CharField(max_length=10, choices=[
    #                                           ("Pending", "En attente"),
    #                                           ("Confirmed", "Confirmé"),
    #                                           ("Cancelled", "Annulé")], 
    #                                           default=Status.PENDING)
    
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    #patient = models.ForeignKey('AccountApp.Patient', on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    