from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=200, blank=False, unique=False)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=False, unique=False)
    user_name = models.CharField(max_length=200, unique=True, blank=False)
    salt = models.CharField(max_length=200, unique=False, blank=False)
    password = models.CharField(max_length=200, unique=False, blank=False)
    created = models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)
