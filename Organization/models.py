from email.mime import application
from msilib.schema import Class
from django.db import models

from User.models import User
from Login.models import Login
import pandas as pd
import csv
from turtle import st
from unicodedata import name
from django.http import HttpResponse
from io import BytesIO


# Create your models here.
class Organization(Login):
    organization_name = models.CharField(max_length=50, primary_key=True)
    organization_address = models.CharField(max_length=50)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def Organization(self, UserID, User_Password, organization_name, organization_address, longitude, latitude):
        obj = Organization(UserID=UserID, User_Password=User_Password, organization_name=organization_name,
                           organization_address=organization_address, longitude=longitude, latitude=latitude)
        obj.save()

    def Check_Employee_Status(self, file):
        csv_file = pd.read_csv(file).to_dict()
        stat = {'user': []}

        for i in range(0, len(csv_file['NID'])):
            try:
                user = User.objects.get(nid=csv_file['NID'][i])

                stat['user'].append([user.nid, user.name, user.Vaccine_status,
                                    user.Covid_Status, user.Frist_Dose, user.Second_Dose, user.Third_Dose])

            except User.DoesNotExist:
                stat['user'].append(
                    ["Invalid NID", "invalid", "invalid", "invalid", "invalid", "invalid", "invalid"])

        return stat
