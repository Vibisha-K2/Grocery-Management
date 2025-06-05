from django.shortcuts import render,redirect
from GroceryApp.models import *
from WebApp.models import *
from django.contrib import messages
import  razorpay

# Create your views here.
def home(request):
    category = CategoryDB.objects.all()
    return render(request,"home.html",{'category':category})
def about(request):
    category = CategoryDB.objects.all()
    return render(request,"about.html",{'category':category})
def products(request):
    product = ProductDB.objects.all()
    category = CategoryDB.objects.all()
    return render(request,"Products.html",{'product':product,'category':category})
def contact(request):
    category = CategoryDB.objects.all()
    return render(request,"contact.html",{'category':category})
def filterd_items(request,cat_name):
    data = ProductDB.objects.filter(Category_Name=cat_name)
    return render(request,"filter.html",{'data':data})
def Single_Product(request,item_id):
    product=ProductDB.objects.get(id=item_id)
    return render(request,"Single_Product.html",{'product':product})
def save_contact(request):
    if request.method=="POST":
        nam=request.POST.get('name')
        ema = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        obj=ContactDB(Name=nam,Email=ema,Subject=sub,Message=msg)
        obj.save()
        messages.success(request,"Thank You...!")
        return redirect(contact)

def sign_in(request):
    return render(request,"sign_in.html")
def sign_up(request):
    return render(request,"sign_up.html")

def save_signup(request):
    if request.method=="POST":
        user =request.POST.get('username')
        pswd = request.POST.get('password')
        con_pass = request.POST.get('confirm')
        eml = request.POST.get('email')
        obj=SignupDB(User_name=user,Password=pswd,Confirm_password=con_pass,Email=eml)
        obj.save()
        messages.success(request,"Registered successfully...!")
        return redirect(sign_up)

def user_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswd = request.POST.get('password')
        if SignupDB.objects.filter(User_name=un,Password=pswd).exists():
            request.session['User_name']=un
            request.session['Password']=pswd
            messages.success(request,"Welcome to our restaurant...!")
            return redirect(home)
        else:
            messages.warning(request,"")
            return redirect(sign_in)
    else:
        messages.warning(request, "")
        return redirect(sign_in)

def user_logout(request):
    del request.session['User_name']
    del request.session['Password']
    return redirect(sign_in)
def save_cart(request):
    if request.method=="POST":
        nam=request.POST.get('user')
        pname = request.POST.get('pro_name')
        quan = request.POST.get('quantity')
        pri = request.POST.get('price')
        tot_pri = request.POST.get('total')
        try:
            x = ProductDB.objects.get(Product_Name=pname)
            img = x.Product_Image
        except ProductDB.DoesNotExist:
            img = None
        obj=CartDB(UserName=nam,Product_Name=pname,Quantity=quan,Price=pri,TotalPrice=tot_pri,Product_Image=img)
        obj.save()
        return redirect(home)

def cart_page(request):
    sub_total = 0
    shipping_amount = 0
    total_amount = 0
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    for i in cart:
        sub_total += i.TotalPrice
        if sub_total > 500:
            shipping_amount = 50
        else:
            shipping_amount = 100
        total_amount = sub_total + shipping_amount
    return render(request,"cart.html",{'cart':cart,'sub_total':sub_total,'shipping_amount':shipping_amount,'total_amount':total_amount})

def delete_cart(request,c_id):
    category=CartDB.objects.filter(id=c_id)
    category.delete()
    return redirect(cart_page)
def checkout_cart(request):
    sub_total = 0
    shipping_amount = 0
    total_amount = 0
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    for i in cart:
        sub_total += i.TotalPrice
        if sub_total > 500:
            shipping_amount = 50
        else:
            shipping_amount = 100
        total_amount = sub_total + shipping_amount
    return render(request, "Checkout.html", {'cart': cart, 'sub_total': sub_total, 'shipping_amount': shipping_amount,
                                         'total_amount': total_amount})

def save_checkout(request):
    if request.method=="POST":
        name=request.POST.get('name')
        plac = request.POST.get('place')
        phone = request.POST.get('phone')
        eml = request.POST.get('email')
        adrs = request.POST.get('address')
        pin = request.POST.get('pincode')
        msg = request.POST.get('message')
        tot = request.POST.get('ototal')
        obj=CheckoutDB(Name=name,Place=plac,Mobile=phone,Email=eml,Address=adrs,Pin_code=pin,Message=msg,TotalPrice=tot)
        obj.save()
        return redirect(payment)

def payment(request):
    customer = CheckoutDB.objects.order_by('-id').first()
    payy = customer.TotalPrice
    amount = int(payy*100)
    payy_str=str(amount)
    if request.method == 'POST':
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_mJFX2vCAoYiHq6','6g0dI0uyVS01hifxfXKuktiA'))
        payment = client.order.create({'amount':amount,'currency':order_currency})
    return render(request,"Payment.html",{'customer':customer,'payy_str':payy_str})