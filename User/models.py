from django.db import models
from django.utils import timezone
import datetime


class user_login(models.Model):

    full_name = models.CharField(max_length=100, default='Uknown')
    email_id =  models.EmailField(default='example@gmail.com')
    mobile_number = models.BigIntegerField(default=000000000)
    password = models.CharField(max_length=12, default='******')
    subscription_id = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'user_login'

    def __int__(self):
        return self.id


class property_details(models.Model):
    user_id = models.CharField(max_length=100, default="Uknown")
    created_date = models.DateField(default=timezone.now, null=True)
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
    property_id = models.IntegerField(default=0)
    district = models.CharField(max_length=100, default="Uknown")
    pin_code = models.BigIntegerField(default=000000)
    address = models.TextField(default="Uknown")
    near_by = models.TextField(default="Uknown")

    class Meta:
        db_table = 'location_details'

    def __int__(self):
        return self.id


class resale_details(models.Model):
    property_id = models.IntegerField(default=0)
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



class amenities(models.Model):
    property_id = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    balcony = models.IntegerField(default=0)
    water_supply = models.CharField(max_length=100, default="Uknown")
    gym = models.CharField(max_length=100, default="Uknown")
    power_backup = models.CharField(max_length=100, default="Uknown")
    gated_security = models.CharField(max_length=100, default="Uknown")
    who_will_show_the_house = models.CharField(max_length=100, default="Uknown")
    secondry_number = models.BigIntegerField(default=000000)
    club_house = models.CharField(max_length=100, default="false")
    swimming_pool = models.CharField(max_length=100, default="false")
    lift = models.CharField(max_length=100, default="false")
    security = models.CharField(max_length=100, default="false")
    children_Play_area = models.CharField(max_length=100, default="false")
    intercom = models.CharField(max_length=100, default="false")
    shoping_center = models.CharField(max_length=100, default="false")
    park = models.CharField(max_length=100, default="false")
    gas_pipeline = models.CharField(max_length=100, default="false")
    internet_provider = models.CharField(max_length=100, default="false")
    fire_safety = models.CharField(max_length=100, default="false")

    class Meta:
        db_table = 'amenities'

    def __int__(self):
        return self.id


class additional_information(models.Model):
    property_id = models.IntegerField(default=0)
    i_want_to_get_my_property_painted = models.CharField(max_length=200, default="Uknown")
    i_want_to_get_my_property_cleaned = models.CharField(max_length=200, default="Uknown")
    do_you_have_all_document = models.CharField(max_length=200, default="Uknown")
    have_you_paid_property_tax = models.CharField(max_length=200, default="Uknown")

    class Meta:
        db_table = 'additional_information'

    def __int__(self):
        return self.id


class schedule(models.Model):
    property_id = models.IntegerField(default=0)
    availablity = models.CharField(max_length=200, default="Uknown")
    start_time = models.TimeField(null=True, default=timezone.now)
    end_time = models.TimeField(null=True, default=timezone.now)

    class Meta:
        db_table = 'schedule'

    def __int__(self):
        return self.id