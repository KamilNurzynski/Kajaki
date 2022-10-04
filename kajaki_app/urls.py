from django.urls import path
from kajaki_app import views

urlpatterns = [
    path('add_route/', views.AddRouteView.as_view(), name='add_route'),
    path('route_list/', views.RouteListView.as_view(), name='route_list'),
    path('add_kayak/', views.AddKayakView.as_view(), name='add_kayak'),
    path('kayak_list/', views.KayakListView.as_view(), name='kayak_list'),
    path('<int:pk>/', views.KayakDetailView.as_view(), name='detail_kayak'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about_us', views.AboutUsView.as_view(), name='about_us'),
    path('update_kayak/<int:pk>/', views.KayakUpdateView.as_view(), name='update_kayak'),
    path('delete_kayak/<int:pk>', views.KayakDeleteView.as_view(), name='delete_kayak'),
]
