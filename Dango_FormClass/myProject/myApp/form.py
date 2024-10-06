

from django import forms

from .models import *



class studentForm(forms.ModelForm):
    class Meta:
        model = studentModel
        fields = ['name','email','depertment']