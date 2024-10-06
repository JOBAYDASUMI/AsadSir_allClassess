

from django.shortcuts import render




def home(req):
    return render(req,'home.html')

def myApp(req):
    return render(req,"temp.html")
