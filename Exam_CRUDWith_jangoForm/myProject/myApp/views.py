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
        Uage=req.POST.get('Uage')
        UDate_of_birth=req.POST.get('UDate_of_birth')
        UImage=req.FILES.get('Uimage')
        U_Type=req.POST.get('U_type')
        Address=req.POST.get('address')
        print(UImage)
        UserModel.objects.create(
            Username=Username,
            Uemail=Email,
            Upassword=Password,
            Uage=Uage,
            UDate_of_birth=UDate_of_birth,
            Uimage=UImage,
            U_type=U_Type,
            address=Address,
        )
        return  redirect("view")
    return render(req,"form.html",{"form":form})




def view(req):
    data=UserModel.objects.all()
    
    return render(req,"view.html",{"data":data})


def EditForm(req,id):
    obj=UserModel.objects.get(id=id)
    form=UserForm(initial={'username':obj.Username,'email':obj.Uemail,'password':obj.Upassword,'Uage':obj.Uage,'UDate_of_birth':obj.UDate_of_birth,'Uimage':obj.Uimage,'U_type':obj.U_type,'address':obj.address})
    if req.method == 'POST':
        Username=req.POST.get('username')
        Email=req.POST.get('email')
        Password=req.POST.get('password')
        Uage=req.POST.get('Uage')
        UDate_of_birth=req.POST.get('UDate_of_birth')
        UImage=req.FILES.get('Uimage')
        U_Type=req.POST.get('U_type')
        Address=req.POST.get('address')
        if UImage:
            img=UImage
        else:
            img=obj.Uimage
        obj=UserModel(
            id=id,
            Username=Username,
            Uemail=Email,
            Upassword=Password,
            Uage=Uage,
            UDate_of_birth=UDate_of_birth,
            Uimage=img,
            U_type=U_Type,
            address=Address,
            )
        
        obj.save()
        return  redirect("view")
    return render(req,"form.html",{"form":form})

def Delete(req,id):
    obj=UserModel.objects.get(id=id).delete()
    return  redirect("view")