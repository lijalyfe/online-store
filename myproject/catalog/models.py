from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Дополнительные поля и методы могут быть добавлены по вашему усмотрению

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # Дополнительные поля и методы могут быть добавлены по вашему усмотрению

