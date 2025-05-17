from django.contrib.auth.models import User
from django.db import models

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    theme = models.CharField(max_length=10, default='light')
    notification_enabled = models.BooleanField(default=True)
    notification_sound = models.CharField(max_length=50, default='default')
    gender = models.CharField(max_length=10, choices=[('male','Male'), ('female','Female'), ('other','Other')])


    def __str__(self):
        return f"{self.name}'s settings"
