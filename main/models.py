from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Agents(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=16)
    home_address = models.CharField(max_length=511)
    work_address = models.CharField(max_length=511)
    key_iv_aes = models.CharField(max_length=128)
    session_key_iv_aes = models.CharField(max_length=128)
    logged_in = models.BooleanField(default=False)
    login_tries = models.PositiveSmallIntegerField()
    confirmed = models.BooleanField(default=False)
    registration_date = models.DateTimeField()

    def __str__(self):
        return self.first_name + " " + self.last_name

    def is_registered_recently(self):
        return self.registration_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)