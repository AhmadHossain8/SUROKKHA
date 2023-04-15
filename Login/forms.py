from django import forms
from django.conf import Settings
from models import *

class User_form(forms.ModelForm):
    User_Password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Login
        fields = ('UserID','User_Password')
    


