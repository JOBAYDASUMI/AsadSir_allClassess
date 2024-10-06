from django.shortcuts import render

from myApp.form import *
from .models import *

def form(req):
    
    
    if req.method =='POST':
        form=studentForm(req.POST)
        if form.is_valid():
            form.save()

    else:
        form = studentForm()
  
        
    return render(req,"form.html",{"form":form})
