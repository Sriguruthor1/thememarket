from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('themes/', views.themes, name='themes'),
    path('template/', views.template_page, name='template'),
    path('login/', views.login_page, name='login'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
]