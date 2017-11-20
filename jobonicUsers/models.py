import uuid

from django.db import models

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200, blank=False, unique=False)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=False, unique=False)
    user_name = models.CharField(max_length=200, unique=True, blank=False)
    salt = models.CharField(max_length=200, unique=False, blank=False)
    password = models.CharField(max_length=200, unique=False, blank=False)
    created = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    organisation = models.CharField(max_length=200, blank=True,default='Jobonics')

    class Meta:
        ordering = ('created',)

class LoginSession (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=200, default=uuid.uuid4, editable=False)
    created = models.IntegerField(default=0)
    expire = models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)


class UserProfile (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=False, blank=False, unique=True)
    email = models.CharField(max_length=100, null=False, blank=False, unique=True)
    address = models.CharField(max_length=150, null=True, blank=True, unique=False)
    marital_status = models.CharField(max_length=50, null=False, blank=False)
    dob = models.IntegerField(default=0)
    nationality = models.CharField(default='Kenyan', max_length=50, blank=False, null=False)
    personal_statement = models.TextField(null=True, blank=True)
    website = models.URLField(max_length=100, null=True, blank=True)
    skills = models.TextField()
    hobbies = models.TextField()

    class Meta:
        ordering = ('dob',)

class Education (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    school = models.CharField(max_length=200, blank=False, null=False)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100, default='to date')

    class Meta:
        ordering = ('user_id', )
