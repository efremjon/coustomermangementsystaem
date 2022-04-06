import imp
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
from .form import OrderForm,CreateUser
from django.forms import inlineformset_factory 
from .filetr import Oredefilters


from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.


def registerPage(request):

    if request.method == "POST":
        form=CreateUser(request.POST)
        if form.is_valid():
            form.save()

            user=form.cleaned_data.get('username')

        
            messages.success(request, 'Account Created Successfuly.'+ user)
            return redirect('login')
    else:
        form=CreateUser()
    context={
        'form':form
    }
    return render(request,'account/reg.html',context)

def loginPage(request):
    context={}
    return render(request,'account/login.html',{})

def logoutUser(request):
    context={}
    return render(request,'account/login.html',{})

def home(request):

    customers=Customer.objects.all()
    Orders=Order.objects.all()
    total_customer=customers.count()
    total_order=Orders.count()
    Deliverd=Orders.filter(status='Delivered').count()
    pending=Orders.filter(status='Pending').count()
    context={
        'customers':customers,
        'Orders':Orders,
        'total_order':total_order,
        'total_customer':total_customer,
        'Deliverd':Deliverd,
        'pending':pending,
    }
   
    return render(request,'account/dashbord.html',context)

def product(request):
    products= Product.objects.all()
    return render(request,'account/product.html',{'products':products})

def customer(request,pk_cust):
    customer=Customer.objects.get(pk=pk_cust)
    Cust_Order=customer.order_set.all()
    total_order=Cust_Order.count()
    MyFileter=Oredefilters(request.GET,queryset=Cust_Order)
    Cust_Order=MyFileter.qs
    context={
        'customer':customer,
        'Cust_Order':Cust_Order,
        'total_order':total_order,
        'MyFileter':MyFileter,
    }
    return render(request,'account/customer.html',context)

def Customer_Order(request, pk):
    OrdeFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=1)
    customersel=Customer.objects.get(pk=pk)
    formset=OrdeFormSet(queryset=Order.objects.none(), instance=customersel)
    
    if request.method == 'POST':
       
        formset=OrdeFormSet(request.POST,instance=customersel)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={
        'formset':formset
    }
    return render(request,'account/customer_order.html',context)

def Update_Order(request, pk):

    order=Order.objects.get(pk=pk)

    if request.method == 'POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=OrderForm(instance=order)
    context={
        'form':form
    }
    return render(request,'account/customer_order.html',context)


def Delete_Order(request, pk):

    item=Order.objects.get(pk=pk)

    if request.method == 'POST':

        item.delete()
        return redirect('/')
    else:
        pass
    
    return render(request,'account/delete.html',{'item':item})