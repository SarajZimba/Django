from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

# Create your views here.
def home(request):
    return render(request, "landingpage.html", {'name': 'Saraz'})

def products(request):
    return render(request, "product.html")

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items_number

    else:
        items=[]
        order = {'get_cart_total': 0, 'get_cart_items_number': 0, 'shipping': False}
        cartItems = order['get_cart_items_number']

    products = product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, "store.html", context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer    
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
       
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items_number
    else:
        items =[]
        order = {'get_cart_total':0, 'get_cart_items_number':0, 'shipping': False}
        cartItems = order['get_cart_items_number']
        #for item in items:
            #count = item.quantity * item.product.price
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, "cart.html", context,)

def login(request):
    return render(request, "loginpage.html")

def register(request):
    return render(request, "register.html")
def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")

def view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items_number

    else:
        items=[]
        order = {'get_cart_total': 0, 'get_cart_items_number': 0, 'shipping': False}
        cartItems = order['get_cart_items_number']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, "view.html", context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print(productId)
    print(action)

    customer = request.user.customer
    productt = product.objects.get(id = productId )
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=productt)


    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def landingpage(request):
    products = product.objects.all()
    context = {'products': products}
    return render(request, "landingpage.html", context)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        customer = request.user.customer
        data = json.loads(request.body)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
            )
    else:
        print('user is not logged in..')
    return JsonResponse('Payment complete', safe=False)