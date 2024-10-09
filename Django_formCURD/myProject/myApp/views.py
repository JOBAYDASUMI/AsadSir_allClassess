from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
 

def formShow(req):
    form=UserForm()
    if req.method == 'POST':
        Username=req.POST.get('username')
        Email=req.POST.get('email')
        Password=req.POST.get('password')
        UserModel.objects.create(
            Username=Username,
            Uemail=Email,
            Upassword=Password,
        )
        return  redirect("view")
    return render(req,"form.html",{"form":form})




def view(req):
    data=UserModel.objects.all()
    
    return render(req,"view.html",{"data":data})


def EditForm(req,id):
    obj=UserModel.objects.get(id=id)
    form=UserForm(initial={'username':obj.Username,'email':obj.Uemail,'password':obj.Upassword})
    if req.method == 'POST':
        Username=req.POST.get('username')
        Email=req.POST.get('email')
        Password=req.POST.get('password')
        obj=UserModel(id=id,Username=Username,Uemail=Email,Upassword=Password)

        obj.save()
        return  redirect("view")
    return render(req,"form.html",{"form":form})

def Delete(req,id):
    obj=UserModel.objects.get(id=id).delete()
    return  redirect("view")