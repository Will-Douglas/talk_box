from django import forms

from django.forms.fields import CharField
from django.forms.widgets import PasswordInput, Textarea

class LogInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150)


class SignUpForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=150)
    password = forms.CharField(widget=PasswordInput)
    profile_name = forms.CharField(min_length=4, max_length=150)
    age = forms.IntegerField()
    hometown = forms.CharField(max_length=125)
    bio = forms.CharField(widget=Textarea)