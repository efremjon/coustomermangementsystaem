from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
from .form import OrderForm
# Create your views here.

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
    context={
        'customer':customer,
        'Cust_Order':Cust_Order,
        'total_order':total_order,
    }
    return render(request,'account/customer.html',context)

def Customer_Order(request):
    if request.method == 'POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=OrderForm()
    context={
        'form':form
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