from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    Name=models.CharField(max_length=100, null=True, blank=True)
    Profile=models.ImageField(upload_to="image", null=True, blank=True)
    Discription=models.CharField(max_length=100, null=True,blank=True)

class ProductDB(models.Model):
    Category_Name=models.CharField(max_length=100, null=True, blank=True)
    Product_Name=models.CharField(max_length=100, null=True, blank=True)
    Discription=models.CharField(max_length=100, null=True, blank=True)
    Price=models.IntegerField(null=True, blank=True)
    Product_Image=models.ImageField(upload_to="image",null=True,blank=True)