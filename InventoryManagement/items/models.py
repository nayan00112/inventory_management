from django.db import models

# Create your models here.

class Categories(models.Model):
    Date_Time = models.DateTimeField(auto_now=True, auto_now_add=False)
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    Status = models.BooleanField(default=True)
    is_modified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Name

class Products(models.Model):
    Date_Time = models.DateTimeField(auto_now=True, auto_now_add=False)
    Name = models.CharField(max_length=50)
    Description = models.TextField()
    Price = models.FloatField()
    Status = models.BooleanField(default=True)
    Categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return self.Name

class Inventory(models.Model):
    Products = models.ForeignKey(Products, on_delete=models.CASCADE)
    Available_Stock = models.IntegerField(default=0)

class Salse_customers(models.Model):
    Date_Time = models.DateTimeField(auto_now=True, auto_now_add=False)
    Transaction_code = models.CharField(max_length=20)
    Customers_name = models.CharField(max_length=50)
    Total_items = models.IntegerField()
    Total_ammount = models.FloatField()
    product_bil_data = models.TextField()
    def __str__(self):
        return self.product_bil_data

