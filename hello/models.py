from django.db import models

# Create your models here.
from django.db import models

class HelloWorld(models.Model):
    message = models.CharField(max_length=100, default="Hello, World!")
 