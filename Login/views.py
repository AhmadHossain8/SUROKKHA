from ast import Or
import imp
from socket import NI_DGRAM
from tabnanny import check
from turtle import home
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from requests import post
from Login.models import Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from Hospital.models import Hospital
from User.models import User
from Organization.models import Organization

# Create your views here.
def Home(request):
    if request.method == 'POST':
        UserID = request.POST['UserID']
        User_Password = request.POST['User_Password']

        obj = Login()
        if obj.verify(UserID):
            hospital_obj = Hospital.objects.filter(UserID = UserID , User_Password = User_Password)
            if hospital_obj.count() > 0:
                hos_obj = Hospital.objects.get(UserID = UserID , User_Password = User_Password)
                request.session['Hos_name'] = hos_obj.Name
                
                return redirect('/Hospital/Home')
            else:
                User_obj = User.objects.filter(UserID = UserID , User_Password = User_Password)

                if User_obj.count() > 0:
                    User_obj = User.objects.get(UserID = UserID , User_Password = User_Password)
                    request.session['user_nid'] = User_obj.nid
                    return redirect('/User/Home')
                else:
                    Org_obj = Organization.objects.filter(UserID = UserID , User_Password = User_Password)
                    if Org_obj.count() > 0:
                        Org_obj = Organization.objects.get(UserID = UserID)
                        request.session['org_id'] = Org_obj.UserID
                        return redirect('/Organization/Home')
                    else:
                        return HttpResponse("Wrong Username Or Password")
        else:
            return HttpResponse(request,"Incorrect User Name or Password")
    return render(request,"Login.html")


def Forgot_Password(request):
    if request.method == 'POST':
        UserID = request.POST['UserID']
        User_Password = request.POST['User_Password']
        obj=Login()
        check = obj.verify(UserID)
        if check == True:
            obj.Forgot_Password(UserID,User_Password)
            return HttpResponse("Password updated!!!")
        else:
            return HttpResponse(request,"Unvalid UserName")
    return render(request,'Forgot_Password.html')
