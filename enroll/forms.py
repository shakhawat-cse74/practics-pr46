from importlib.metadata import requires
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {'name':'Enter Name :','email':'Enter Email :' , 'password':'Enter Password'}
        widgets = {'password':forms.PasswordInput }
        
        