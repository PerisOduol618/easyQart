from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm

from .models import *

# Create your views here.
def registerPage(request):
    form = UserCreationForm()
   
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'accounts/register.html' , context)


def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html' , context)