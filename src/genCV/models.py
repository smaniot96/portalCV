from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Generation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_data = models.TextField()
    output_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
