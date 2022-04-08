
from django.forms import ModelForm
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name','email','username','password1','password2']