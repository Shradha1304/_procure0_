

from django.contrib import admin
from django.urls import path
from . import views
from .views import index
from .views import Login , logout

from .views import CheckOut



urlpatterns = [
    path("",views.index, name="index"),
    
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path("cart/",views.cart , name="cart"),
    path("order/",views.order , name="order"),
    
    path('check-out', views.CheckOut , name='checkout'),
    path("track/",views.tracker, name="tracker"),
    path("search/",views.search, name="search"),
    path("checkout/",views.check, name="checkout"),
    path("productview/",views.proview, name="see"),
]
