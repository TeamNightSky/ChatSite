from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    cookie = models.CharField(max_length=256)
    verified = models.BooleanField()
    verification_expiration = models.IntegerField()
    hash = models.CharField(max_length=256)
