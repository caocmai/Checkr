from django.db import models

# Create your models here.

class NasaImage(models.Model):
    image = models.ImageField(upload_to="pics")