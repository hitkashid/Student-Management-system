from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    error = ""
    if request.method == "POST":
        first = request.POST['firstname']
        last = request.POST['lastname']
        code = request.POST['empcode']
        email = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=first, last_name=last, username=email, password=pwd)
            EmployeeDetail.objects.create(User=user, empcode=code)
            error = "no"
        except:
            error = "yes"

    return render(request, 'registration.html', locals())


def login_f(request):
    error = ""
    if request.method == "POST":
        un = request.POST["email"]
        pwd = request.POST["password"]
        a = authenticate(username=un, password=pwd)
        if a:
            login(request, a)
            error = "no"
        else:
            error = "yes"

    return render(request, 'login_page.html', locals())


def profile(request):
    error = ""
    user = request.user
    emp = EmployeeDetail.objects.get(User=user)
    if request.method == "POST":
        first = request.POST['firstname']
        last = request.POST['lastname']
        code = request.POST['empcode']
        email = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=first, last_name=last, username=email, password=pwd)
            EmployeeDetail.objects.create(User=user, empcode=code)
            error = "no"
        except:
            error = "yes"

    return render(request, 'profile.html', locals())


def home(request):
    return render(request, 'home_page.html')


def logo(request):
    logout(request)
    return redirect(index)
