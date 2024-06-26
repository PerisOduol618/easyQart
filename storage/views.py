import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm

from .models import *

# Authentication
def registerPage(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()

    if request.method == 'POST':
        form = UserCreationForm()

    context = {'form':form}
    return render(request, 'accounts/register.html' , context)


def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html' , context)

def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
      
    if 'q' in request.GET:
        q = request.GET['q']
        products = Product.objects.filter(name__icontains=q)
    else:
        products = Product.objects.all()

    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    # set conditions fro an authenticated user and one for a user the is not logged in
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order.get_cart_items

    context = {'items':items, 'order':order,'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order.get_cart_items

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    # send post request
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Product:', productId)
    print('Action:',action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('item was added', safe=False)