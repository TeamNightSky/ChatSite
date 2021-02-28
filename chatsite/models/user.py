from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    cookie = models.CharField(max_length=256)

