from django.urls import path
from . import views

urlpatterns = [
    # authentication
    path('register/', views.registerPage, name = 'register'),
    path('login/', views.loginPage, name = 'login'),

    
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_Item/', views.updateItem, name="updateItem"),

]