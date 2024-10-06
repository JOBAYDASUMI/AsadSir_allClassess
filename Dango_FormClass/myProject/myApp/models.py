from django.db import models

class studentModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    depertment=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f"{self.name}-{self.depertment}"
