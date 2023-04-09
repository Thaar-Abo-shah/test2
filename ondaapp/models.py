from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50,null=True) 
    email = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=10,null=True)
    level = models.CharField(max_length=20,null=True)
    type = models.CharField(max_length=20,null=True)
    image_after = models.ImageField(upload_to='images/',null=True)
    image_before = models.ImageField(upload_to='images/',null=True)
    date= models.DateField(null=True)

    class Meta:
        app_label= 'ondaapp'
 
 
    def __str__(self):
         return self.name