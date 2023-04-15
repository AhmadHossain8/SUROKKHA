from tabnanny import check
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from Hospital.models import Hospital
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from Login.models import Login
from User.models import User

#from User.models import User
# Create your views here.

data = {
"Name" : [],
"Address" : [],
"Number_of_Vaccine_Per_Day" : [],
"Vaccine" : [],
"email" : [],
"Seat_Capacity_For_COVID_Testing" : [],
"longitude" : [],
"latitude" : []
}
def Home(request):
    Name = request.session['Hos_name']
    obj = Hospital.objects.get(Name = Name)
    data['Name'] = obj.Name
    data['Address'] = obj.Address
    data['Number_of_Vaccine_Per_Day'] = obj.Number_of_Vaccine_Per_Day
    data['Vaccine'] = obj.Vaccine
    data['email'] = obj.email
    data['Seat_Capacity_For_COVID_Testing'] = obj.Seat_Capacity_For_COVID_Testing
    data['longitude'] = obj.longitude
    data['latitude'] = obj.latitude

    posts4 = User.objects.filter(Covid_Test_Hospital = Name)
    post1 = User.objects.filter(hospital_name = Name)
    print(post1)
    return render(request,'Hospital/Hospital_Home.html', {'data' : data,'posts4':posts4,'post1' : post1})


def Regstration_Hospital(request):
    if request.method=='POST':
        Name = request.POST['Name']
        Address=request.POST['Address']
        Number_of_Vaccine_Per_Day = request.POST['Number_of_Vaccine_Per_Day']
        Seat_Capacity_For_COVID_Testing = request.POST['Seat_Capacity_For_COVID_Testing']
        UserID=request.POST['UserID']
        User_Password=request.POST['User_Password']
        email = request.POST['email']
        Vaccine = request.POST['Vaccine']
        longitude = request.POST['long']
        latitude = request.POST['lat']
        obj = Hospital()
        if obj.verify(UserID) == True:
            return HttpResponse(request,"Try New User")
        else :
            obj.Hospital(UserID,User_Password,Name,Address,Number_of_Vaccine_Per_Day,Vaccine,email,Seat_Capacity_For_COVID_Testing,longitude,latitude)
            return redirect('http://127.0.0.1:8000/')
    return render(request,"Hospital/signup.html")


def Update_Number_of_Vaccine(request):
    value = request.POST['Number_of_Vaccine_Per_Day']
    obj = Hospital()
    check = obj.Update_Number_of_Vaccine(value,request.session['Hos_name'])    
    if check == False:
        check = "Update Failed"
    else:
        check = "Updated"
    return HttpResponse(check)

def Update_Vaccine(request):
    value = request.POST['Vaccine']
    obj = Hospital()
    check = obj.Update_Vaccine(value,request.session['Hos_name'])    
    if check == False:
        check = "Update Failed"
    else:
        check = "Updated"
    return HttpResponse(check)


def Update_Covid_Testing_Capacity(request):
    value = request.POST['test_Per_Day']
    obj = Hospital()
    check = obj.Update_Covid_Testing_Capacity(value,request.session['Hos_name'])    
    if check == False:
        check = "Update Failed"
    else:
        check = "Updated"
    return HttpResponse(check)

def Update_User_Test_Result(request):
    value = request.POST['covid_status']
    nid = request.POST['nid']
    obj = User.objects.get(nid = nid)
    obj.Covid_Status  = value
    obj.save()
    return HttpResponse("Success")


def Update_User_Test_date(request):
    value = request.POST['covid_date']
    nid = request.POST['nid']
    obj = User.objects.get(nid = nid)
    obj.Covid_Test_Date  = value
    obj.save()
    return HttpResponse("Success")


def Update_User_Vaccine_Info(request):
    value = request.POST['vaccine_status']
    nid = request.POST['nid']
    obj = User.objects.get(nid = nid)
    obj.Vaccine_status = value
    obj.save()
    return HttpResponse("Success")








