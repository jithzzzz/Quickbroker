"""Realproperty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Admin import views as ad
from User import views as us
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('admin-login', ad.login),
    path('admin-login-form/', ad.login_form),
    path('admin-register', ad.register),
    path('admin-register-form/', ad.register_form),
    path('Dashboard/', ad.dashboard),
    path('subscriptio-view-form/', ad.subscriptio_view_form),
    path('submit-subscription-plan', ad.submit_subscription_plan),

    # User
    path('', us.index),
    path('user-login', us.user_login_check),
    path('home/', us.home),
    path('sell-property/', us.sell_property),
    path('new-post-form/', us.new_post_form),
    path('property-details-submit', us.property_details_submit),

]
