from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=60)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=gender_choices, blank=False)
    
    preference = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    interest = models.CharField(max_length=1, choices=preference, blank=False)

    age = models.IntegerField(
        default=18,
        validators=[MaxValueValidator(100), MinValueValidator(18)],
        blank=False
    )

    bio = models.TextField(max_length=256, blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)