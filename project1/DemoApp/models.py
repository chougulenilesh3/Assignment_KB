from django.db import models

# Create your models here.
class UserRegistrationModel(models.Model):
    username = models.CharField( max_length = 32)
    email = models.CharField(max_length = 32,)
    password = models.CharField(max_length = 32,)
    
 #jjhmjhhjkhkjhkjuhy
