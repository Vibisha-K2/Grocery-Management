from django.shortcuts import render,redirect
from GroceryApp.models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"Index.html")
def add_category(reqeust):
    return render(reqeust,"Add_category.html")

def save_category(request):
    if request.method=="POST":
        name=request.POST.get('name')
        img = request.FILES['image']
        discription = request.POST.get('disc')
        obj=CategoryDB(Name=name,Profile=img,Discription=discription)
        obj.save()
        messages.success(request,"Category saved successfully...!")
        return redirect(add_category)

def display_category(reqeust):
    cats=CategoryDB.objects.all()
    return render(reqeust,"Display_category.html",{'cats':cats})

def edit_category(request,cat_id):
    data=CategoryDB.objects.get(id=cat_id)
    return render(request,"Edit_Category.html",{'data':data})

def update_category(request,data_id):
    if request.method == "POST":
        name = request.POST.get('name')
        discription=request.POST.get('disc')
        # img=request.FILES['image']
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=CategoryDB.objects.get(id=data_id).Profile
        CategoryDB.objects.filter(id=data_id).update(Name=name,Profile=file,Discription=discription)
        return redirect(display_category)

def delete_category(request,c_id):
    category=CategoryDB.objects.filter(id=c_id)
    category.delete()
    return redirect(display_category)

#**********************************************************************************************************

def add_product(request):
    cat=CategoryDB.objects.all()
    return render(request,"Add_product.html",{'category':cat})
def save_product(request):
    if request.method=="POST":
        cat_name=request.POST.get('category')
        pro_name=request.POST.get('product')
        discription = request.POST.get('disc')
        price=request.POST.get('price')
        img=request.FILES['image']
        obj=ProductDB(Category_Name=cat_name,Product_Name=pro_name,
                      Discription=discription,Price=price,Product_Image=img)
        obj.save()
        messages.success(request, "Product saved successfully...!")
        return redirect(add_product)

def display_product(request):
    product=ProductDB.objects.all()
    return render(request,"Display_Product.html",{'product':product})

def delete_product(request,d_id):
    product=ProductDB.objects.filter(id=d_id)
    product.delete()
    return redirect(display_product)
def edit_product(request,pro_id):
    cat=CategoryDB.objects.all()
    pro=ProductDB.objects.get(id=pro_id)
    return render(request,"Edit_Product.html",{'pro':pro,'cat':cat})
def update_product(request,data_id):
    if request.method == "POST":
        cat_name = request.POST.get('category')
        pro_name = request.POST.get('product')
        discription=request.POST.get('disc')
        price=request.POST.get('price')
        # img=request.FILES['image']
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name, img)
        except MultiValueDictKeyError:
            file=ProductDB.objects.get(id=data_id).Product_Image
        ProductDB.objects.filter(id=data_id).update(Category_Name=cat_name,Product_Name=pro_name,
                                Discription=discription,Price=price,Product_Image=file)
        return redirect(display_product)

#Login page
def admin_login(request):
    return render(request,"Admin_login.html")

def admin_login_page(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pswd)
            if x is not None:
                request.session['username'] = un
                request.session['password'] = pswd

                login(request,x)
                return redirect(index)
            else:
                return redirect(admin_login)
        else:
            return redirect(admin_login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)

def contact_details(request):
    data = ContactDB.objects.all()
    return render(request,"Contact_details.html",{'data':data})

def delete_contact(request,con_id):
    Contact=ContactDB.objects.filter(id=con_id)
    Contact.delete()
    return redirect(contact_details)