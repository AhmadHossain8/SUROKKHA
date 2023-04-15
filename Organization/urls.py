from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
   path('',views.Registration),
   path('Home',views.Home),
   path('user_status',views.user_status)
]