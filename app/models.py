from dis import show_code
from django.db import models
from .utils import random_string_generator

# Create your models here.

class Url(models.Model):
    origin_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=6)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code=random_string_generator(6)
        super(Url, self).save(*args, **kwargs)

    def __str__(self):
        return self.short_code
                  