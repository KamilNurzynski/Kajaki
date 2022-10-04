from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from accounts.forms import LoginForm, CreateUserForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from kajaki_app.models import Kayak, Route, Order, OrderKayak


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html', {'form': LoginForm(), 'submit_value_text': 'Zaloguj się'})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                login(request, user)
                url = request.GET.get('next', reverse('index'))
                return redirect(url)
        return render(request, 'accounts/login.html', {'form': LoginForm(), 'submit_value_text': 'Zaloguj się'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class RegisterView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'accounts/create_user.html', {'form': form, 'submit_value_text': 'Zarejestruj się'})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # tworzy pustego usera
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
        return render(request, 'accounts/create_user.html', {'form': form, 'submit_value_text': 'Zarejestruj się'})


class UserAccountView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        orders = Order.objects.filter(buyer=user).order_by('-date')
        orders_kayak = OrderKayak.objects.all()
        return render(request, 'accounts/my_account.html', {'user': user, 'orders': orders, 'orders_kayak': orders_kayak})
