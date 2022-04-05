from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'account/dashbord.html',{})

def product(request):
    return render(request,'account/product.html',{})

def customer(request):
    return render(request,'account/customer.html',{})

