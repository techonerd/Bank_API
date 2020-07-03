from django.db import models

# Create your models here.
class Bank(models.Model):
    ifsc = models.CharField(max_length=11)
    bank_id	= models.IntegerField()
    branch	= models.CharField(max_length=74)
    address	= models.TextField()
    city	= models.CharField(max_length=50)
    district	= models.CharField(max_length=50)
    state	= models.CharField(max_length=26)
    bank_name= models.CharField(max_length=50)
    
    def __str__(self):
        return self.ifsc