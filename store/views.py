from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from .category import Category
from django.template import loader
from django.shortcuts import render
from django.utils import timezone
from math import ceil
from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from .customer import Customer
from django.views import  View


# Create your views here.

def index(request):
    products=product.objects.all()
    print(products)
    n=len(products)
    nSlides=n//4+ceil((n/4)-(n//4))
    params={'no. of Slides':nSlides,'range':range(1 ,nSlides),  'product': products}
    #allpro=[[products,range(1,len(products)),nSlides],[products,range(1,len(products)),nSlides]]
    #params={'allpro':allpro}
    return render(request ,'index.html',params)


class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')

def cart(request):
    return render(request ,'cart.html')

def order(request):
    return render(request ,'order.html')


def tracker(request):
    return HttpResponse('we r at tracker')


def search(request):
    return HttpResponse('we r at search')

def check(request):
    return HttpResponse('we r at checkout')

def proview(request):
    return HttpResponse('we are at product view')