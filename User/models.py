from msilib.schema import Class
from tokenize import Name
from django.db import models
from requests import request
from Hospital.models import Hospital
from Login.models import Login
from Vaccination_Info.models import Vaccination_Info
import datetime as DT
import pandas as pd
import csv
from turtle import st
from unicodedata import name
from django.http import HttpResponse
from io import BytesIO
# Create your models here.


class User(Login, Vaccination_Info):
    nid = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=500)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=50)
    flat_no = models.CharField(max_length=50)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    email = models.CharField(max_length=100, null=True)
    Covid_Test_Date = models.DateField(null=True)
    Covid_Status = models.CharField(max_length=150, null=True)
    Covid_Test_Hospital = models.ForeignKey(
        Hospital, null=True, on_delete=models.SET_NULL)

    def User(self, UserID, User_Password, nid, name, date_of_birth, address, flat_no, longitude, latitude, email):
        hos_name = Hospital.objects.get(Name='default')
        obj = User(email=email, UserID=UserID, User_Password=User_Password, nid=nid, name=name, date_of_birth=date_of_birth, address=address, flat_no=flat_no,
                   longitude=longitude, latitude=latitude, Covid_Test_Hospital=hos_name, hospital_name=hos_name, Covid_Status='N/A', Vaccine_status='N/A')
        obj.save()

    def Apply_for_Test(self, hospital, nid):
        today = DT.date.today()
        day = today + DT.timedelta(days=2)
        hos_obj = Hospital.objects.get(Name=hospital)
        cnt = User.objects.filter(
            Covid_Test_Hospital=hos_obj, Covid_Test_Date=day).count() + 1
        cnt1 = Hospital.objects.get(
            Name=hos_obj.Name).Seat_Capacity_For_COVID_Testing
        if cnt > cnt1:
            return False
        else:
            obj = User.objects.get(nid=nid)
            obj.Covid_Test_Hospital = hos_obj
            obj.Covid_Test_Date = day
            obj.save()
            return True

    def Apply_for_Vaccine(self, hospital, nid):
        today = DT.date.today()
        first_dose = today + DT.timedelta(days=2)
        Second_dose = today + DT.timedelta(days=32)
        Third_dose = today + DT.timedelta(days=212)
        hos_obj = Hospital.objects.get(Name=hospital)
        default_obj = Hospital.objects.get(Name='default')

        if not(User.objects.filter(hospital_name=default_obj, nid=nid).exists()):
            return False

        cnt1 = User.objects.filter(
            hospital_name=hos_obj.Name, Frist_Dose=first_dose).count() + 1
        cnt2 = User.objects.filter(
            hospital_name=hos_obj.Name, Second_Dose=Second_dose).count() + 1
        cnt3 = User.objects.filter(
            hospital_name=hos_obj.Name, Third_Dose=Third_dose).count() + 1
        cntx = Hospital.objects.get(
            Name=hos_obj.Name).Number_of_Vaccine_Per_Day

        if cnt1 > cntx or cnt2 > cntx or cnt3 > cntx:
            return False
        else:
            obj = User.objects.get(nid=nid)
            obj.hospital_name = hos_obj
            obj.Frist_Dose = first_dose
            obj.Second_Dose = Second_dose
            obj.Third_Dose = Third_dose
            obj.save()
            return True

    def Met_People_Today(self, file):
        csv_file = pd.read_csv(file).to_dict()
        stat = {'user': []}

        for i in range(0, len(csv_file['NID'])):
            try:
                user = User.objects.get(nid=csv_file['NID'][i])
                if user.Covid_Status == 'False' or user.Covid_Status == 'N/A':
                    stat['user'].append([user.name, "Do not need quarantine"])
                else:
                    stat['user'].append([user.name, "Need quarantine"])
            except User.DoesNotExist:
                stat['user'].append(["invalid", "invalid"])
        return stat
