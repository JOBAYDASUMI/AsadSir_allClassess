from django.db import models

# Create your models here.
class UserModel(models.Model):
    Username=models.CharField(max_length=100)
    Uemail=models.EmailField()
    Upassword=models.CharField(max_length=8)

    def __str__(self):
        return self.Username
