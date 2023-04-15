from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('Home', views.Home),
    path('Registration',views.Regstration_Hospital,name = 'Registration'),
    path('Update_Number_of_Vaccine/',views.Update_Number_of_Vaccine,name='Update_Number_of_Vaccine'),
    path('Update_Vaccine/',views.Update_Vaccine,name='Update_Vaccine'),
    path('Update_Covid_Testing_Capacity/',views.Update_Covid_Testing_Capacity,name = 'Update_Covid_Testing_Capacity'),
    path('Update_User_Test_Result/',views.Update_User_Test_Result,name = 'Update_User_Test_Result/'),
    path('Update_User_Test_date/',views.Update_User_Test_date,name = 'Update_User_Test_date/'),
    path('Update_User_Vaccine_Info/',views.Update_User_Vaccine_Info,name = 'Update_User_Vaccine_Info')
]




