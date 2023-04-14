from django.conf import settings
from django.db import models
from django.utils import timezone


class QR(models.Model):
    image = models.ImageField(upload_to='qr_codes/')

    def __str__(self):
        return self.image.name