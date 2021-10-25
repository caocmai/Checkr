from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class NasaImage(models.Model):
    image = models.ImageField(upload_to="pics")

class Rating(models.Model):
    username = models.ForeignKey(User, on_delete=models.PROTECT)
    nasaImage = models.ForeignKey(NasaImage, on_delete=CASCADE)
    stars = models.IntegerField(help_text='Rate the number of stars for this image', validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    def __str__(self):
        return self.stars
