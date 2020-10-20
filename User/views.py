from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q

from User.models import user_login, resale_details, location_details, property_details, amenities,\
     additional_information, schedule
from Admin.models import subscription_plans as sp


def index(request):
    subscription_plans = sp.objects.filter(status=True).\
        values('pk', 'status', 'plan_name', 'ad_active_time', 'dedicated_chat', 'monthly_price', 'dedicated_phone', 'service_charge', 'number_of_ad_month',\
            'commision_less_25_lack', 'commision_more_25_lack', 'commision_more_50_lack')
    print(list(subscription_plans))

    return render(request, 'index.html', {'subscription_plans': subscription_plans})


def user_login_check(request):
    if request.method == 'POST':
        try:
            email = request.POST['login_email']
            password =  request.POST['login_password']
            print(email)
            print(password)
            # checking session is active then navigating to dashboard
            if request.session.has_key('user_session_login'):
                return HttpResponse('Login Succes')
            else:
                if user_login.objects.filter(Q(email_id=email) & Q(password=password)).count() > 0:
                    request.session['user_session_login'] = email
                    # request.session.set_expiry(10)
                    return HttpResponse('Login Succes')
                else:
                    return HttpResponse('Error')
        except Exception as e:
            print(e)
            return HttpResponse('login')


def home(request):
    return render(request, 'home.html')


def sell_property(request):
    return render(request, 'sell-property.html')


def new_post_form(request):
    if request.session.has_key('user_session_login'):
        user_details = user_login.objects.get(email_id=request.session['user_session_login'])
        subscripbed_plan = sp.objects.get(pk=user_details.subscription_id)
    print(subscripbed_plan.number_of_image_per_ads)
    return render(request, 'postadd.html', {'Number_of_images': range(0, subscripbed_plan.number_of_image_per_ads)})


def property_details_submit(request):
    if request.method == 'POST':
        try:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            Apartment_Type = request.POST['Apartment_Type']
            bhk_Type = request.POST['BHK_Type']
            Ownership_Type = request.POST['Ownership_Type']
            Built_Up_Area = request.POST['Built_Up_Area']
            Property_Age = request.POST['Property_Age']
            Facing = request.POST['Facing']
            Floor_Type = request.POST['Floor_Type']
            Floor = request.POST['Floor']
            Total_Floor = request.POST['Total_Floor']
            print("******************************")
            ad_id = property_details.objects.create(apartment_type=Apartment_Type, bhk_type=bhk_Type, ownership=Ownership_Type, \
                built_up_area=Built_Up_Area, property_age=Property_Age, facing=Facing, floor_type=Floor_Type, floor=Floor,\
                      total_floor=Total_Floor, user_id=request.session['user_session_login'])
            print(ad_id.pk)
            
            return JsonResponse({'Status':True, 'id':ad_id.pk})
        except Exception as e:
            print(e)
            return JsonResponse({'Status':False, 'Error':e})


def location_details_submit(request):
    if request.method == 'POST':
        try:
            ads_id = request.POST['ads_id']
            District = request.POST['District']
            Pin_Code = request.POST['Pin_Code']
            Address = request.POST['Address']
            Near_By = request.POST['Near_By']
            location_id = location_details.objects.create(property_id=ads_id, district=District, pin_code=Pin_Code, \
                address=Address, near_by=Near_By)
            return JsonResponse({'Status':True})
        except Exception as e:
            return JsonResponse({'Status':False, 'Error':e})


def resale_details_submit(request):
    if request.method == 'POST':
        try:
            ads_id = request.POST['ads_id']
            Expected_Price = request.POST['Expected_Price']
            Maintenance_Cost = request.POST['Maintenance_Cost']
            Available_From = request.POST['Available_From']
            Kitchen_Type = request.POST['Kitchen_Type']
            Furnishining = request.POST['Furnishining']
            Kitchen_Type = request.POST['Kitchen_Type']
            Parking = request.POST['Parking']
            Description = request.POST['Description']

            resale_id = resale_details.objects.create(property_id=ads_id, expected_price=Expected_Price, maintenance_cost=Maintenance_Cost, \
                available_from=Available_From, kitchen_type=Kitchen_Type, furnishining=Furnishining, parking=Parking, description=Description)
            return JsonResponse({'Status':True})
        except Exception as e:
            return JsonResponse({'Status':False, 'Error':e})


def amenities_submit(request):
    if request.method == 'POST':
        try:
            ads_id = request.POST['ads_id']
            Bathroom = request.POST['Bathroom']
            Balcony = request.POST['Balcony']
            Water_supply = request.POST['Water_supply']
            Gym = request.POST['Gym']
            Power_Backup = request.POST['Power_Backup']
            Gated_security = request.POST['Gated_security']
            Who_will_show_the_house = request.POST['Who_will_show_the_house']
            Secondry_Number = request.POST['Secondry_Number']
            Club_House = request.POST['Club_House']
            Swimming_Pool = request.POST['Swimming_Pool']
            Lift = request.POST['Lift']
            Security = request.POST['Security']
            Children_Play_Area = request.POST['Children_Play_Area']
            Intercom = request.POST['Intercom']
            Shoping_Center = request.POST['Shoping_Center']
            Park = request.POST['Park']
            Gas_Pipeline = request.POST['Gas_Pipeline']
            Internet_Provider = request.POST['Internet_Provider']
            Fire_Safety = request.POST['Fire_Safety']

            print(Bathroom)
            print("##################################")

            amenities_id = amenities.objects.create(property_id=ads_id, bathrooms=Bathroom, balcony=Balcony, water_supply=Water_supply,\
                gym=Gym, power_backup=Power_Backup, gated_security=Gated_security, who_will_show_the_house=Who_will_show_the_house, secondry_number=Secondry_Number,\
                    club_house=Club_House, swimming_pool=Swimming_Pool, lift=Lift, security=Security, children_Play_area=Children_Play_Area,\
                        intercom=Intercom, shoping_center=Shoping_Center, park=Park, gas_pipeline=Gas_Pipeline, internet_provider=Internet_Provider,\
                            fire_safety=Fire_Safety)
            return JsonResponse({'Status':True})
        except Exception as e:
            return JsonResponse({'Status':False, 'Error':e})


def additional_information_submit(request):
    if request.method == 'POST':
        try:
            ads_id = request.POST['ads_id']
            I_want_to_get_my_property_painte = request.POST['_want_to_get_my_property_painte']
            I_want_to_get_my_property_cleaned = request.POST['I_want_to_get_my_property_cleaned']
            Do_you_have_all_document = request.POST['Do_you_have_all_document']
            Have_you_paid_property_tax = request.POST['Have_you_paid_property_tax']

            additional_information_id = additional_information.objects.create(property_id=ads_id, i_want_to_get_my_property_painted=I_want_to_get_my_property_painte,\
                i_want_to_get_my_property_cleaned=I_want_to_get_my_property_cleaned, do_you_have_all_document=Do_you_have_all_document, have_you_paid_property_tax= Have_you_paid_property_tax)
            return JsonResponse({'Status':True})
        except Exception as e:
            return JsonResponse({'Status':False, 'Error':e})



def Schedule_information_submit(request):
     if request.method == 'POST':
        try:
            ads_id = request.POST['ads_id']
            Availablity = request.POST['Availablity']
            Start_Time = request.POST['Start_Time']
            End_Time = request.POST['End_Time']
            schedule_id = schedule.objects.create(property_id=ads_id, availablity=Availablity, start_time=Start_Time, end_time=End_Time)
            return JsonResponse({'Status':True})
        except Exception as e:
            return JsonResponse({'Status':False, 'Error':e})


