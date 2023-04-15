from turtle import right
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from Hospital.models import Hospital
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from Login.models import Login
from User.models import User
from Hospital.models import Hospital
from Vaccination_Info.views import DownloadPDF, ViewPDF
import pandas as pd
import csv
from turtle import st
from unicodedata import name
from django.http import HttpResponse
from io import BytesIO

# Create your views here.
data = {
    "nid": [],
    "name": [],
    "date_of_birth": [],
    "address": [],
    "flat_no": [],
    "covid_status": [],
    "vaccine_status": [],
    "covid_test_date": [],
    "first_dose": [],
    "second_dose": [],
    "third_dose": []
}


def Home(request):
    nid = request.session['user_nid']
    obj = User.objects.get(nid=nid)
    data['address'] = obj.address
    data['name'] = obj.name
    data['nid'] = obj.nid
    data['date_of_birth'] = obj.date_of_birth
    data['flat_no'] = obj.flat_no
    data['covid_status'] = obj.Covid_Status
    data['vaccine_status'] = obj.Vaccine_status
    data['covid_test_date'] = obj.Covid_Test_Date
    data['first_dose'] = obj.Frist_Dose
    data['second_dose'] = obj.Second_Dose
    data['third_dose'] = obj.Third_Dose
    name = Hospital.objects.values_list('Name', flat=True)
    hospital_name = []
    for star in name.iterator():
        if star == 'default':
            continue
        hospital_name.append(star)

    return render(request, 'User/User_Home.html', {'data': data, 'hospital_name': hospital_name})


def Registration_User(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        UserID = request.POST['UserID']
        User_Password = request.POST['User_Password']
        email = request.POST['email']
        longitude = request.POST['long']
        latitude = request.POST['lat']
        nid = request.POST['nid']
        flat_no = request.POST['flat_no']
        date_of_birth = request.POST['date_of_birth']
        obj = User()
        if obj.verify(UserID) == True:
            return HttpResponse(request, "Try New User")
        else:
            obj.User(UserID, User_Password, nid, name, date_of_birth,
                     address, flat_no, longitude, latitude, email)
            return redirect('http://127.0.0.1:8000/')
    return render(request, "User/signup.html")


def pdf(request):
    return redirect(ViewPDF)


def download(request):
    return redirect(DownloadPDF)


def Apply_Test(request):
    if request.method == 'POST':
        test_hospital = request.POST['hos_test']
        obj = User()
        check = obj.Apply_for_Test(test_hospital, data['nid'])
        if check == False:
            check = "Try another Hospital"
        else:
            check = "Successful"
        return HttpResponse(check)


def Apply_Vaccine(request):
    if request.method == 'POST':
        test_hospital = request.POST['hos_vaccine']
        obj = User()
        check = obj.Apply_for_Vaccine(test_hospital, data['nid'])
        if check == False:
            check = "Try another Hospital or you have already been registered"
        else:
            check = "Successful"
        return HttpResponse(check)


def user_status(request):
    obj = User()
    file = request.FILES["csv_file"]
    stat = obj.Met_People_Today(file)
    print(stat)
    for i in stat:
        print(type(i))

    return render(request, 'User/user_status.html', {'stat': stat})
