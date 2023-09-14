from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.category_name




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', default='product-default.png')
    description = models.TextField()
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.01'))])
    countInStock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.01'))])
    numReviews = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

