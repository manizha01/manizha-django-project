from django.db import models

# Create your models here.

class client(models.Model):
    CITY_CHOICES = [('ON','Toronto'),('ON','Missisauga'),('ON','Milton'), ('NY', 'New York'), ('ON','Brampton')]
    COUNTRY_CHOICES = [('CA','Canada'),('USA','United State of America'),('EU','Europe')]
    first = models.CharField(max_length=43)
    last = models.CharField(max_length = 31)
    email = models.CharField(max_length=31)
    company = models.CharField(max_length=50 , blank = True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=21, choices = CITY_CHOICES,)
    country = models.CharField(max_length=33, choices=COUNTRY_CHOICES,)
    phone = models.CharField(max_length=31, null=True)

    dress = models.ManyToManyField('dress')

def __str__(self):
    return self.first

#new class for dress
class dress(models.Model):
    size = models.CharField(max_length= 9)

def __str__(self):
    return self.size

   
   




    


