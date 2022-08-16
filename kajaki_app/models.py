# from django.contrib.auth.models import User
from django.db import models
from accounts.models import User


class Contact(models.Model):
    text = models.TextField()
    author = models.EmailField()  # jak dla zalogowanego i dla niezalogowanego
    date = models.DateTimeField(auto_now_add=True)


# dwa rodzaje kajaków: 1os i 2os
class Kayak(models.Model):
    name = models.CharField(max_length=123)
    description = models.TextField()
    # photo = models.ImageField() dodaj jak bedzie czas
    price_addition = models.FloatField() # lub multiplier
    # typ kajaku


class Route(models.Model):
    name = models.CharField(max_length=255)
    map = models.URLField()  # czy to tak?????????????????????? Dodawanie tagu <iframe> lub textfield
    price = models.FloatField()
    description = models.TextField()

class OrderKayak(models.Model):
    kayak = models.ForeignKey(Kayak)
    order  = models.ForeignKey("Order")
    amount = models.IntegerField(default=1)


class Order(models.Model):
    date = models.DateField()
    kayaks = models.ManyToManyField(Kayak, on_delete=models.CASCADE, through='OrderKayak')

    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    total_order_price = models.FloatField()
    buyer = models.ForeignKey(User)

    def get_parce(self):
        OK = self.orderkayak_set.all()
        suma = 0
        for item in OK:
            suma += item.amount*self.route.price+item.amount*item.kayak.price_addition
        return suma

    class Meta:
        unique_together = ('kayak', 'date')
class CartKayak:
    pass

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kayaks = models.ManyToManyField(Kayak, on_delete=models.CASCADE, through='CartKayak')
    route =


    def get_total_price(self):
        pass
    # jak zapisać zakceptowanie transakcji i przesłanie pieniędzy
