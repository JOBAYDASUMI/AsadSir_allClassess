from django import forms

class UserForm(forms.Form):
    username=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField(max_length=8,widget=forms.PasswordInput)