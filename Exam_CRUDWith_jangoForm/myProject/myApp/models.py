from django.db import models

class UserModel(models.Model):
    OPTIONS=[
        ('student','Student'),
        ('jobHolder','Jobholder'),
    ]
    Username=models.CharField(max_length=100)
    U_type=models.CharField(max_length=100,null=True,choices=OPTIONS)
    Uemail=models.EmailField()
    Upassword=models.CharField(max_length=8)
    UDate_of_birth=models.DateField(null=True)
    Uage=models.CharField(max_length=100)
    Uimage=models.ImageField(upload_to="U_pic/",null=True)
    address=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.Username
