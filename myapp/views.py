import re
from django.shortcuts import render ,redirect
from .models import *
from .form import *
# Create your views here.

def index(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        Employee.objects.create(name=name, email=email, country=country)
        return redirect('home')
    return render(request,"index.html")

def home(request):
    user = Employee.objects.all()
    users = {
        'users' : user
    }
    return render(request,"home.html",context = users)

def remove(request,id):
    if(Employee.objects.get(id=id)):
        Employee.objects.get(id=id).delete()
    return redirect("home")

def edit(request,id):
    user = Employee.objects.get(id=id)
    if(request.method=="POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        user.name = name
        user.email = email
        user.country = country
        user.save()
        return redirect('home')
    users = {
        'user' : user,
    }
    return render(request, 'edit.html',context=users)