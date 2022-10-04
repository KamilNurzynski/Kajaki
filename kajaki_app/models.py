# from django.contrib.auth.models import User
from django.db import models
from accounts.models import User


class Contact(models.Model):
    subject = models.CharField(max_length=255)
    text = models.TextField()
    author = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)


class Kayak(models.Model):
    name = models.CharField(max_length=123)
    type = models.CharField(max_length=255)
    description = models.TextField()
    photo_url = models.URLField()
    # photo = models.ImageField() #dodaj jak bedzie czas
    price_addition = models.FloatField()  # lub multiplier

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=255)
    map_url = models.URLField()
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    kayaks = models.ManyToManyField(Kayak, through='OrderKayak')
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def get_price(self):
        OK = self.orderkayak_set.all()
        suma = 0
        for item in OK:
            suma += item.amount * self.route.price + item.amount * item.kayak.price_addition
        return suma


class OrderKayak(models.Model):
    kayak = models.ForeignKey(Kayak, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
