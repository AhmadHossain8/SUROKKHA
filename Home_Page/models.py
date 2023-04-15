from django.db import models
from msilib.schema import CheckBox
from urllib import response
from click import confirm
from django.http import HttpResponse
from django.shortcuts import render
from pandas import value_counts
import requests
import json
import datetime as DT

# Graph data 
url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
newheaders = {
	"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com",
	"X-RapidAPI-Key": "43442304b8mshd3e52abe82d6647p13c505jsn0eac43c951b5"
}

# Create your models here.
class Chart_Data(models.Model):
    date = models.DateField(null=True)
    confirmed = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    
    def Houndred_Days_Info(self):
        today = DT.date.today()
        for i in range(1,100):
            day = today - DT.timedelta(days=i)
            querystring = {"date":day}
            day = requests.request("GET", url, headers=newheaders, params=querystring)
            day = json.loads(day.text)
            obj = Chart_Data(date = day['data']['date'], confirmed = day['data']['confirmed'],deaths = day['data']['deaths'])
            obj.save()




