from django.db import models


# Create your models here.

class User(models.Model):
    fullName = models.CharField(max_length= 255)
    company = models.CharField(max_length= 255)
    email = models.EmailField()
    password = models.CharField(max_length=255)



    def __str__(self):
        return self.fullName

    
class Subscription(models.Model):
    package = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    monthlyPrice = models.CharField(max_length = 255)
    yearlyPrice = models.CharField(max_length =255)


    def __str__(self):
        return self.name


