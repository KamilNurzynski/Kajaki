from django.urls import reverse
from accounts.forms import LoginForm
from kajaki_app.forms import AddRouteForm, AddKayakForm, ContactForm
from kajaki_app.models import Kayak, Route, Contact, Order, OrderKayak
import pytest


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


def test_login_view_get(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, LoginForm)


@pytest.mark.django_db
def test_login_view_post(client, user_login):
    url = reverse('login')
    response = client.post(url, user_login)
    assert response.status_code == 302
    assert response.url == reverse('index')


@pytest.mark.django_db
def test_login_view_post_redirect_to_next(client, user_login):
    url = reverse('login')
    url += "?next=" + reverse('add_kayak')
    response = client.post(url, user_login)
    assert response.status_code == 302
    assert response.url == reverse('add_kayak')


@pytest.mark.django_db
def test_add_route_view_get(client):
    url = reverse('add_route')
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, AddRouteForm)


@pytest.mark.django_db
def test_add_route_view_post(client):
    url = reverse('add_route')
    data = {
        'name': 'Poniatówka-zoo',
        'map_url': 'https://www.google.com/maps/d/embed?mid=18n8wowePh2K45zDNuznyjIPaKEjTsDw&ehbc=2E312F',
        'price': '60',
        'description': 'Trasa prowadząca przez odcinek Warszawa Śródmieście.'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Route.objects.get(**data)


@pytest.mark.django_db
def test_route_list_view(client):
    url = reverse('route_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_kayak_view_get(client):
    url = reverse('add_kayak')
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, AddKayakForm)


@pytest.mark.django_db
def test_add_kayak_view_post(client):
    url = reverse('add_kayak')
    data = {
        'name': 'Jadowity',
        'type': '1 osobowy',
        'description': 'jakis text',
        'photo_url': 'http://rospuda.pl/wp-content/uploads/2017/04/fit_147_pe.png',
        'price_addition': '40'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Kayak.objects.get(**data)


@pytest.mark.django_db
def test_kayak_list_view(client):
    url = reverse('kayak_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_kayak_view(client, user, kayak):
    url = reverse('update_kayak', args=(kayak.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_kayak_view(client, user, kayak):
    url = reverse('delete_kayak', args=(kayak.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_view_get_not_login(client):
    url = reverse('order')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_order_view_get_login(client, user):
    url = reverse('order')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_view_post_login(client, user, route, kayak):
    url = reverse('order')
    data = {
        'user': user,
        'route': route,
        'date': '2022-12-22',
        'kayak': kayak,
        'amount': '12'
    }
    data_for_order = {
        'route': route,
        'buyer': user,
        'date': '2022-12-22'
    }
    client.force_login(user)
    response = client.post(url, data)
    assert response.status_code == 302
    order = Order.objects.get(**data_for_order)
    assert order
    data_for_order_kayak = {
        'kayak': kayak,
        'order': order,
        'amount': '12'
    }
    assert OrderKayak.objects.get(**data_for_order_kayak)
    assert response.url == reverse('my_account')


@pytest.mark.django_db
def test_contact_view_get(client):
    url = reverse('contact')
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, ContactForm)


@pytest.mark.django_db
def test_contact_view_post(client):
    url = reverse('contact')
    data = {
        'subject': 'Temat',
        'text': 'opis',
        'author': 'nurzynski.kamil@gmail.com'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Contact.objects.get(**data)


@pytest.mark.django_db
def test_about_us_view_get(client):
    url = reverse('about_us')
    response = client.get(url)
    assert response.status_code == 200
