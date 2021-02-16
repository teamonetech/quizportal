"""Quiz_Project URL Configuration

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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [

    path('index/' , views.index),
    path('signup/',views.signup),
    path('login/',views.login),
    path('',views.userloginview),
    path('aboutus/',views.aboutus),
    path('forgot/',views.forgot,name='forgot'),
    path('userregister/',views.userregister,name='userregister'),
    path('userloginview/',views.userloginview,name='userloginview'),
    path('userauthentication/',views.userauthentication),
    path('userhome/',views.userhome,name='userhome'),
    path('logoutuser/',views.logoutuser),
    path('quizquestions/',views.quizquestions,name='quizquestions'),
    path('forgotpass/',views.forgotpass,name='forgotpass'),
    path('changepassview/',views.changepassview,name='changepassview'),
    path('changepass/',views.changepass),
    path('result/',views.result,name="result"),
    path('passstudentsview/',views.passstudentsview,name='passstudents'),
    path('passstudents/',views.passstudents,name='pass'),
    path('quizquestions/',views.quizquestions,name='quizquestions'),
    path('quizquestions1/',views.quizquestions1),
    path('quizquestions2/',views.quizquestions2),
    path('quizresult/',views.quizresult),
    path('passstudentslist/',views.passstudentslist),
    path('download/',views.download),
    path('profile/',views.profile),
    path('profile_details/',views.profile_details),
    path('testlogin/',views.testlogin),
    path('export/',views.export),
    path('demo/',views.demo),
    path('instructions1/',views.instructions1),
    path('instructions2/',views.instructions2),
    path('account/',include('django.contrib.auth.urls')),



]

