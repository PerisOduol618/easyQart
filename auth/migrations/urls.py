from django.urls import path
from . import views

urlpatterns = [
    
    path('register/', views.registerPage,  {'next_page': '/store/'}, name = 'register'),
    path('login/', views.loginPage, {'next_page': '/store/'}, name = 'login'),

]