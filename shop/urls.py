from django.contrib import admin
from django.urls import path
from shop import views as shop
from django.contrib.staticfiles.urls import static

app_name = 'shop'
urlpatterns = [
    path('home', shop.home_view, name='home_page'),
    path('login', shop.login_view, name='login_page'),
    path('register', shop.register_view, name='register_page'),
    path('buy/<int:idIten>/', shop.buy_view, name='buy_page'),
    path('purchase', shop.purchase_view, name='purchase_page'),
    path('logout', shop.logout_view, name='logout_page'),

]