from django.db import models

# Create your models here.

from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title