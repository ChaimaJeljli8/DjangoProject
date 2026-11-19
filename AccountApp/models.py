

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.

class Specialty(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    # Add any additional fields you want for the user model
    #user_id = models.CharField(primary_key=True) si on veut personnaliser l'identifiant de l'utilisateur ou le redefinir
    pass

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    phone = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Specialties = models.ManyToManyField(
        "AccountApp.Specialty",
        related_name="doctors")


number_Validator= RegexValidator(
                regex=r'^\d{8}$', 
                message="This number must contain 8 digits."
            )

def validate_birth_date(v):
    if v >= timezone.localdate() :
        raise ValidationError("La date de naissance n'est pas valide.")
    
class Patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[number_Validator]) #redefinition de l'identifiant 
    phone = models.CharField(max_length=8, validators=[number_Validator])
    birth_date = models.DateField(Validators=[validate_birth_date])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



