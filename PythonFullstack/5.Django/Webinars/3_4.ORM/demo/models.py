from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.brand}, {self.model}: {self.color}'

class Person(models.Model):
    name = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='owners')

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=50)

class Order(models.Model):
    products = models.ManyToManyField(Product, related_name='orders', through='OrderPosition')

class OrderPosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
    quantity = models.IntegerField()
