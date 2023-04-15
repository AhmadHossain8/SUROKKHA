from django.http import HttpResponse
from django.shortcuts import redirect, render
from Organization.models import Organization
import pandas as pd
import csv
from turtle import st
from unicodedata import name
from django.http import HttpResponse
from io import BytesIO

# Create your views here.


def Home(request):
    UserID = request.session['org_id']
    obj = Organization.objects.filter(UserID=UserID).only
    return render(request, "Organization/Organization_Home.html", {'posts': obj})


def Registration(request):
    if request.method == 'POST':
        organization_name = request.POST['organization_name']
        organization_address = request.POST['organization_address']
        organization_password = request.POST['organization_password']
        organization_userid = request.POST['organization_UserID']
        longitude = request.POST['long']
        latitude = request.POST['lat']
        obj = Organization()
        obj.Organization(organization_userid, organization_password,
                         organization_name, organization_address, longitude, latitude)
        return redirect('http://127.0.0.1:8000/')

    return render(request, "Organization/signup.html")


def user_status(request):
    obj = Organization()
    file = request.FILES["csv_file"]
    stat = obj.Check_Employee_Status(file)
    print(stat)
    return render(request, 'Organization/user_status.html', {'stat': stat})
