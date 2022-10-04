from django.contrib import admin
from .models import Kayak, Route, Contact, Order, OrderKayak

admin.site.register(Kayak)
admin.site.register(Route)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderKayak)