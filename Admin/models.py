from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Admin_Profile(models.Model):
    full_name = models.CharField(max_length=100, default='Uknown')
    email_id =  models.EmailField(default='example@gmail.com')
    mobile_number = models.BigIntegerField(default=000000000)
    gender = models.CharField(max_length=100, default='None')
    password = models.CharField(max_length=12, default='******')

    class Meta:
        db_table = 'admin_profile'

    def __int__(self):
        return self.id


class subscription_plans(models.Model):
    plan_name = models.CharField(max_length=100, default='Uknown')
    ad_active_time = models.IntegerField(default=0)
    dedicated_chat = models.BooleanField(default=False)
    dedicated_phone = models.BooleanField(default=False)
    number_of_ad_month = models.IntegerField(default=0)
    commision_less_25_lack = models.IntegerField(default=0)
    commision_more_25_lack = models.IntegerField(default=0)
    commision_more_50_lack = models.IntegerField(default=0)
    monthly_price = models.BigIntegerField(default=0.00)
    service_charge = models.BigIntegerField(default=0.00)
    number_of_image_per_ads = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'subscription_plans'

    def __int__(self):
        return self.id


