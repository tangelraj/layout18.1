from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('cat/', views.cat, name='cat'),
    path('checkout1/', views.checkout1, name='checkout1'),
    path('consult/', views.consult, name='consult'),
    path('consult1/', views.consult1, name='consult1'),
    path('dog/', views.dog, name='dog'),
    path('login/', views.login, name='login'),
    path('petservice/', views.petservice, name='petservice'),
    path('smallpet/', views.smallpet, name='smallpet'),
    path('thank/', views.thank, name='thank'),
]
