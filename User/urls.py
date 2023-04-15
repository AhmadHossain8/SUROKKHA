from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.Registration_User),
    path('Home',views.Home,name = 'Home'),
    path('pdf',views.pdf,name = 'pdf'),
    path('download',views.download,name = 'download'),
    path('Apply_Test/',views.Apply_Test,name = 'Apply_Test/'),
    path('Apply_Vaccine/',views.Apply_Vaccine,name = 'Apply_Vaccine/'),
    path('user_status/',views.user_status,name = 'user_status/'),
]



