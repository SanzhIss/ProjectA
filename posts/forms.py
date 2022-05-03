from django import forms
from .models import *

GChoices = (('M', 'Male'), ('F', 'Female'),)


class CreateUser(forms.ModelForm):
    class Meta:
        model = RegUser
        fields = "__all__"
