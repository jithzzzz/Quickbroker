from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q

from User.models import user_login, resale_details, location_details, property_details
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
    return render(request, 'postadd.html')


def property_details_submit(request):
    if request.method == 'POST':
        try:
            Apartment_Type = request.POST['Apartment_Type']
            bhk_Type = request.POST['BHK_Type']
            Ownership_Type = request.POST['Ownership_Type']
            Built_Up_Area = request.POST['Built_Up_Area']
            Property_Age = request.POST['Property_Age']
            Facing = request.POST['Facing']
            Floor_Type = request.POST['Floor_Type']
            Floor = request.POST['Floor']
            Total_Floor = request.POST['Total_Floor']
            property_details.objects.create(apartment_type=Apartment_Type, bhk_type=bhk_Type, )
            return JsonResponse({'Status':True})
        except Exception as e:
            return JsonResponse({'Status':False, 'Error':e})
