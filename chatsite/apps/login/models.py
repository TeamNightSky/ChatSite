from django.db import models


class LoginSession(models.Model):
    user_id = models.IntegerField(primary_key=True)
    rand = models.IntegerField()
    valid_resp = models.CharField(max_length=256)
