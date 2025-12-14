from django.shortcuts import render
from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class ProductDepartment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()    
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(ProductDepartment, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.name
    
class ProductPurchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase - {self.product.name}"
    
class ProductSell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale - {self.product.name}"    