
from django.shortcuts import render, redirect
from . models import bankkk
from . forms import *
from django.contrib import messages
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def new(request):
    return render(request,'new.html')
def page(request):
    form=BankForm
    mydict={
        'form':form
    }


    return render(request,'form.html',context=mydict)
def message(request):
    return render(request,'msg.html')