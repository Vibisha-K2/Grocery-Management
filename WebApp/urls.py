from django.urls import path
from WebApp import views

urlpatterns=[
    path('home/',views.home,name="home"),
    path('about/', views.about, name="about"),
    path('products/', views.products, name="products"),
    path('contact/', views.contact, name="contact"),
    path('filterd_items/<cat_name>', views.filterd_items, name="filterd_items"),
    path('Single_Product/<int:item_id>/', views.Single_Product, name="Single_Product"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('', views.sign_in, name="sign_in"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('save_signup/', views.save_signup, name="save_signup"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('delete_cart/<int:c_id>/', views.delete_cart, name="delete_cart"),
    path('checkout_cart/', views.checkout_cart, name="checkout_cart"),
    path('save_checkout/', views.save_checkout, name="save_checkout"),
    path('payment/', views.payment, name="payment"),

]