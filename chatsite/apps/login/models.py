from django.db import models


class LoginSession(models.Model):
    user_id = models.IntegerField(primary_key=True)
    rand = models.CharField(max_length=32)
    valid_resp = models.CharField(max_length=256)

    def __str__(self):
        return "<User: {} | Rand: {} | Valid resp: {}>".format(
            self.user_id,
            self.rand,
            self.valid_resp[:10]
        )


class CaptchaSession(models.Model):
    reg_id = models.IntegerField(primary_key=True)
    sentence = models.CharField(max_length=96)
    index = models.IntegerField()
    verified = models.BooleanField()
