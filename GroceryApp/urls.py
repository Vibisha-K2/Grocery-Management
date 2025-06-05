from django.urls import path
from GroceryApp import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('add_category/', views.add_category, name="add_category"),
    path('save_category/', views.save_category, name="save_category"),
    path('display_category/', views.display_category, name="display_category"),
    path('edit_category/<int:cat_id>/', views.edit_category, name="edit_category"),
    path('update_category/<int:data_id>/', views.update_category, name="update_category"),
    path('delete_category/<int:c_id>/', views.delete_category, name="delete_category"),

    #********************************************************************************************

    path('add_product/', views.add_product, name="add_product"),
    path('save_product/', views.save_product, name="save_product"),
    path('display_product/', views.display_product, name="display_product"),
    path('delete_product/<int:d_id>/', views.delete_product, name="delete_product"),
    path('edit_product/<int:pro_id>/', views.edit_product, name="edit_product"),
    path('update_product/<int:data_id>/', views.update_product, name="update_product"),

    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_login_page/', views.admin_login_page, name="admin_login_page"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('contact_details/', views.contact_details, name="contact_details"),
    path('delete_contact/<int:con_id>/', views.delete_contact, name="delete_contact"),

]
