from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=150)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.category_name




class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name= models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='products', default='product-default.png')
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.01'))])
    numReviews = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, validators=[MinValueValidator(Decimal('0.01'))])
    countInStock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    createdAl = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment= models.TextField(null=True, blank=True)
       

    class Meta:
        verbose_name = ("Review")
        verbose_name_plural = ("Reviews")

    def __str__(self):
        return self.rating
    
    
class Order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, blank=True, null=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    shippingPrice=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    totalPrice=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    
    
    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return self.createdAt

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    qty = models.IntegerField(null=True, blank=False, default=0)
    price=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    image = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = ("OrderItem")
        verbose_name_plural = ("OrderItems")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("OrderItem_detail", kwargs={"pk": self.pk})

 