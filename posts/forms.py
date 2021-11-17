from django import forms
from django.forms.fields import CharField
from django.forms.widgets import Textarea

from nu_talker.models import NuTalker

class PostForm(forms.Form):
    body = forms.CharField(widget=Textarea)