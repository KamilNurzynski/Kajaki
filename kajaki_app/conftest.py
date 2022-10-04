import pytest
from django.contrib.auth.models import User
from kajaki_app.models import Kayak, Route, Contact


@pytest.fixture
def user_login():
    data = {
        'username': 'testowy',
        'password': 'alamakota'
    }
    User.objects.create_user(**data)
    return data


@pytest.fixture
def user():
    data = {
        'username': 'testowy',
        'password': 'alamakota'
    }
    u = User.objects.create_user(**data)
    return u


@pytest.fixture
def user():
    data = {
        'username': 'testowy',
        'password': 'alamakota'
    }
    u = User.objects.create_user(**data)
    return u


@pytest.fixture
def kayak():
    return Kayak.objects.create(name="Jadowity", type="1 osobowy", description='Jakiś tekst',
                                photo_url='http://rospuda.pl/wp-content/uploads/2017/04/fit_147_pe.png',
                                price_addition=40)


@pytest.fixture
def route():
    return Route.objects.create(name='poniatówka-zoo',
                                map_url='https://www.google.com/maps/d/embed?mid=18n8wowePh2K45zDNuznyjIPaKEjTsDw&ehbc=2E312F',
                                price=100, description='Trasa prowadząca przez odcinek Warszawa Śródmieście.')




# @pytest.fixture
# def movies(category, persons):
#     lst = []
#     for x in range(10):
#         m = Film()
#         m.title = x
#         m.year = 1990
#         m.category = category
#         m.director = persons[0]
#         m.screenwriter = persons[1]
#         m.save()
#         lst.append(m)
#     return lst
