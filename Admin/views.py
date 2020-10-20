from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q

from Admin.models import Admin_Profile, subscription_plans


# Create your views here.

def login_form(request):
    return render(request, 'admin_ogin.html')


def login(request):
    if request.method == 'POST':
        try:
            email = request.POST['login_email']
            password =  request.POST['login_password']
            # checking session is active then navigating to dashboard
            if request.session.has_key('user_id'):
                print("%%%%%%%%")
                return HttpResponse('Login Succes')
            else:
                print("*********")
                if Admin_Profile.objects.filter(Q(email_id=email) & Q(password=password)).count() > 0:
                    print("&&&&&&")
                    request.session['user_id'] = email
                    # request.session.set_expiry(10)
                    return HttpResponse('Login Succes')
                else:
                    return HttpResponse('Error')
        except Exception as e:
            print("@@@@@")
            print(e)
            return HttpResponse('login')


def register_form(request):
    return render(request, 'admin_register.html')


def register(request):
    if request.method == 'POST':
        try:
            name =  request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            gender = request.POST['gender']
            password = request.POST['password']
            if Admin_Profile.objects.filter(email_id=email).count() > 0:
                return HttpResponse('Account Already Exist !!!')
            else:
                Admin_Profile.objects.create(full_name=name, email_id=email, mobile_number=mobile, gender=gender, password=password)
                return HttpResponse("OK")
        except Exception as e:
            return HttpResponse(e)


def dashboard(request):
    if request.session.has_key('user_id'):
        print("%%%%%%%% #######################")
        return render(request, 'dashboard.html')
    else:
        return render(request, 'admin_login.html')


def subscriptio_view_form(request):
    return render(request, 'subscription.html')


def submit_subscription_plan(request):
    if request.method == 'POST':
        try:
            plan_name = request.POST['plan_name']
            status = request.POST['status']
            active_time = int(request.POST['active_time'])
            no_post_month = int(request.POST['no_post_month'])
            c_25 = float(request.POST['c_25'])
            c_more_25 = float(request.POST['c_more_25'])
            c_more_50 = float(request.POST['c_more_50'])
            sub_price = int(request.POST['sub_price'])
            service_charge = int(request.POST['service_charge'])
            chat_support =  request.POST['chat_support']
            phone_support = request.POST['phone_support']
            image_per_ad = request.POST['image_per_ad']
            print("&&&&&&&&&&&&&&&&&&&&&&&&")
            subscription_plans.objects.create(plan_name=plan_name, ad_active_time=active_time, dedicated_chat=chat_support, 
            dedicated_phone=phone_support, number_of_ad_month=no_post_month, commision_less_25_lack=c_25, commision_more_25_lack=c_more_25,
            commision_more_50_lack=c_more_50, monthly_price=sub_price, service_charge=service_charge, status=status, number_of_image_per_ads=image_per_ad)
            return JsonResponse({'Status': True, 'Message': 'New Plan Created'})

        except Exception as e:
            return JsonResponse({'Status': False, 'Error': e})