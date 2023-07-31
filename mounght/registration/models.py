from django.db import models
from django.contrib.auth.models import User

class RegistrationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
