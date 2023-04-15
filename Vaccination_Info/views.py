import csv
from turtle import st
from unicodedata import name
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.db import connection
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import pandas as pd
import datetime as DT
from User.models import User
from Vaccination_Info.models import Vaccination_Info

data = {
"nid" : [],
"name" : [],
"date_of_birth" : [],
"address" : [],
"flat_no" : [],
"covid_status" : [],
"vaccine_status" : [],
"First_Dose":[],
"Second_Dose":[],
"Third_Dose":[],

}


def ViewPDF(request):
	nid = request.session['user_nid']
	obj = User.objects.get(nid = nid)
	data['address'] = obj.address
	data['name'] = obj.name
	data['nid'] = obj.nid
	data['date_of_birth'] = obj.date_of_birth
	data['flat_no'] = obj.flat_no
	data['covid_status'] = obj.Covid_Status
	data['vaccine_status'] = obj.Vaccine_status
	data['First_Dose']=obj.Frist_Dose
	data['Second_Dose']=obj.Second_Dose
	data['Third_Dose']=obj.Third_Dose
	obj = Vaccination_Info()
	return obj.ViewPDF(data)



#Automaticly downloads to PDF file
def DownloadPDF(request):
	nid = request.session['user_nid']
	obj = User.objects.get(nid = nid)
	data['address'] = obj.address
	data['name'] = obj.name
	data['nid'] = obj.nid
	data['date_of_birth'] = obj.date_of_birth
	data['flat_no'] = obj.flat_no
	data['covid_status'] = obj.Covid_Status
	data['vaccine_status'] = obj.Vaccine_status
	data['First_Dose']=obj.Frist_Dose
	data['Second_Dose']=obj.Second_Dose
	data['Third_Dose']=obj.Third_Dose
	obj = Vaccination_Info()
	return obj.DownloadPDF(data)