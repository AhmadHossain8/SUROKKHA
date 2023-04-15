from msilib.schema import Class
from django.db import models
from django.http import HttpResponse

# Create your models here.

class Login(models.Model):
    UserID = models.CharField(max_length=100,primary_key = True)
    User_Password = models.CharField(max_length=100)
    
    def Login(self,UserID,User_Password):
        obj = Login(UserID = UserID, User_Password = User_Password)
        obj.save()
    
    def verify(self,UserID):
        try:
            obj = Login.objects.get(UserID = UserID)
            return True
        except Login.DoesNotExist:
            return False

    def Forgot_Password(self,UserID,User_Password):
            obj=Login(UserID=UserID)
            obj.User_Password=User_Password
            obj.save()
            return HttpResponse("Password updated!!!")

