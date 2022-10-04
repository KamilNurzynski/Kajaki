from django.shortcuts import render, redirect
from kajaki_app.models import Route, Kayak, Order, OrderKayak
from django.urls import reverse, reverse_lazy
from datetime import date
from django.views import View
from kajaki_app.forms import AddKayakForm, AddRouteForm, ContactForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin


class AddRouteView(View):
    # permission_required = ['kajaki_app.add_route']

    def get(self, request):
        form = AddRouteForm()
        return render(request, 'kajaki_app/add_route.html', {'form': form, 'submit_value_text': 'Dodaj'})

    def post(self, request):
        form = AddRouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_route'))
        return render(request, 'kajaki_app/add_route.html', {'form': form, 'submit_value_text': 'Dodaj'})


class RouteListView(ListView):
    model = Route
    template_name = 'kajaki_app/route_list.html'


class AddKayakView(View):
    # permission_required = ['kajaki_app.add_kayak']

    def get(self, request):
        form = AddKayakForm()
        return render(request, 'kajaki_app/add_kayak.html', {'form': form, 'submit_value_text': 'Dodaj'})

    def post(self, request):
        form = AddKayakForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_kayak'))
        return render(request, 'kajaki_app/add_kayak.html', {'form': form, 'submit_value_text': 'Dodaj'})


class KayakListView(ListView):
    model = Kayak
    template_name = 'kajaki_app/kayak_list.html'


class KayakUpdateView(LoginRequiredMixin, UpdateView):
    # permission_required = ['filmy.change_film']

    model = Kayak
    template_name = 'kajaki_app/add_kayak.html'
    fields = '__all__'

    def get_success_url(self):
        super().get_success_url()
        return reverse("add_kayak", args=(self.object.id,))


class KayakDeleteView(LoginRequiredMixin, DeleteView):
    model = Kayak
    template_name = 'kajaki_app/kayak_delete.html'
    success_url = reverse_lazy('kayak_list')


class KayakDetailView(DetailView):
    model = Kayak
    template_name = 'kajaki_app/details_kayak.html'


class CheckoutView(View):
    def get(self, request):
        return render(request, 'kajaki_app/checkout.html')

    def post(self, request):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        date = request.POST.get('date', '')
        phone = request.POST.get('phone', '')

        return render(request, 'kajaki_app/checkout.html')


class OrderView(LoginRequiredMixin, View):
    def get(self, request):
        routes = Route.objects.all()
        kayaks = Kayak.objects.all()
        return render(request, 'kajaki_app/order.html', {'kayaks': kayaks, 'routes': routes})

    def post(self, request):
        user = request.user
        route = request.POST.get('route')
        date = request.POST.get('date')
        kayak = request.POST.get('kayak')
        amount = request.POST.get('amount')
        if route and date and int(amount) >= 1 and kayak:
            route = Route.objects.get(name=route)
            order = Order.objects.create(route=route, buyer=user, date=date)
            kayak = Kayak.objects.get(name=kayak)
            order_kayak = OrderKayak.objects.create(kayak=kayak, order=order, amount=amount)
            return redirect(reverse('my_account'))
        return render(request, 'kajaki_app/order.html', {'message': 'Wypełnij poprawnie wszystkie pola'})


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'kajaki_app/contact.html', {'form': form, 'submit_value_text': 'Wyślij'})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        return render(request, 'kajaki_app/contact.html', {'form': form, 'submit_value_text': 'Wyślij'})


class AboutUsView(View):
    def get(self, request):
        return render(request, 'kajaki_app/about_us.html')
