import email
from email.mime import application
from msilib.schema import Class
from xmlrpc.client import boolean
from django.db import models
from Login.models import Login


# Create your models here.
class Hospital(Login):
    Name = models.CharField(max_length=200,primary_key=True)
    Address = models.CharField(max_length=200)
    Number_of_Vaccine_Per_Day = models.IntegerField(default=0)
    Vaccine = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    Seat_Capacity_For_COVID_Testing = models.IntegerField(default=0)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    
    def Hospital(self,UserID,User_Password,Name,Address,Number_of_Vaccine_Per_Day,Vaccine,email,Seat_Capacity_For_COVID_Testing,longitude,latitude):
        obj = Hospital(UserID = UserID,User_Password = User_Password ,Name = Name , Address = Address , Number_of_Vaccine_Per_Day = Number_of_Vaccine_Per_Day,
        Vaccine = Vaccine ,email = email , Seat_Capacity_For_COVID_Testing = Seat_Capacity_For_COVID_Testing , longitude = longitude , latitude = latitude)
        obj.save()
    

    def Update_Number_of_Vaccine(self,value,name):
        obj = Hospital.objects.get(Name = name)
        obj.Number_of_Vaccine_Per_Day = value
        obj.save()
        return True

    def Update_Vaccine(self,value,name):
        obj = Hospital.objects.get(Name = name)
        obj.Vaccine = value
        obj.save()
        return True

    def Update_Covid_Testing_Capacity(self,value,name):
        obj = Hospital.objects.get(Name = name)
        obj.Seat_Capacity_For_COVID_Testing = value
        obj.save()
        return True



