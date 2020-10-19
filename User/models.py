from django.db import models
from django.utils import timezone
import datetime


class user_login(models.Model):

    full_name = models.CharField(max_length=100, default='Uknown')
    email_id =  models.EmailField(default='example@gmail.com')
    mobile_number = models.BigIntegerField(default=000000000)
    password = models.CharField(max_length=12, default='******')
    
    class Meta:
        db_table = 'user_login'

    def __int__(self):
        return self.id


class property_details(models.Model):
    apartment_type = models.CharField(max_length=100, default="Uknown")
    bhk_type = models.CharField(max_length=100, default="Uknown")
    ownership = models.CharField(max_length=100, default="Uknown")
    built_up_area = models.BigIntegerField(default=000000)
    property_age = models.CharField(max_length=100, default="Uknown")
    facing = models.CharField(max_length=100, default="Uknown")
    floor_type  = models.CharField(max_length=100, default="Uknown")
    floor = models.CharField(max_length=100, default="Uknown")
    total_floor = models.CharField(max_length=100, default="Uknown")

    class Meta:
        db_table = 'Property_Details'

    def __int__(self):
        return self.id



class location_details(models.Model):
    district = models.CharField(max_length=100, default="Uknown")
    pin_code = models.BigIntegerField(default=000000)
    address = models.TextField(default="Uknown")
    near_by = models.TextField(default="Uknown")

    class Meta:
        db_table = 'location_details'

    def __int__(self):
        return self.id


class resale_details(models.Model):
    expected_price = models.BigIntegerField(default=000000)
    maintenance_cost = models.BigIntegerField(default=000000)
    available_from = models.CharField(max_length=100, default="00-00-0000")
    kitchen_type = models.CharField(max_length=100, default="Uknown")
    furnishining = models.CharField(max_length=100, default="Uknown")
    parking = models.CharField(max_length=100, default="Uknown")
    description = models.TextField(default="Uknown")

    class Meta:
        db_table = 'resale_details'

    def __int__(self):
        return self.id