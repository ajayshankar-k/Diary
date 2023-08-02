from django.shortcuts import render,redirect,get_object_or_404
from datetime import date
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.template.defaultfilters import date as date_filter

def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword'] 
        if User.objects.filter(username=email).exists():
            messages.error(request,'Email already registered !!!',extra_tags='error')
            return redirect('index')
        elif password == repassword:
            obj = User()
            obj.username = email
            obj.password = make_password(password)
            obj.save()
            messages.success(request,'Registration Success !!!',extra_tags='success')
            return redirect('signin')
        else:
            messages.error(request,'Both password should be same !!!',extra_tags='error')
            return redirect('index')
    else:
        return render(request,'index.html')
    
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            user = User.objects.get(username=email)
            if user.check_password(password):
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,'Incorrect password !!!',extra_tags='error')
                return redirect('signin')
        else:
            messages.error(request,'Incorrect email !!!',extra_tags='error')
            return redirect('signin')
    else:
        return render(request,'signin.html')
    
def signout(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def dashboard(request):
    user = request.user
    logged = user.username
    events = Events.objects.filter(email=logged).order_by('-date')
    return render(request,'dashboard.html',{'logged':logged,'events':events})

@login_required(login_url='signin')
def add_event(request):
    current_date = date.today()  
    formatted_date = current_date.strftime('%Y-%m-%d')
    user = request.user
    logged = user.username
    if request.method == 'POST':
        title = request.POST['title']
        dates = request.POST['date']
        context = request.POST['context']
        obj = Events()
        obj.title = title
        obj.date = dates
        obj.context = context
        obj.email = logged
        obj.save()
        return redirect('dashboard')
    else:
        return render(request,'add_event.html',{'formatted_date':formatted_date})

@login_required(login_url='signin')
def edit_event(request,id):
    data = get_object_or_404(Events,id=id)
    if request.method=='POST':
        title = request.POST['title']
        dates = request.POST['date']
        context = request.POST['context']
        Events.objects.filter(id=id).update(title=title,date=dates,context=context)
        return redirect('dashboard')
    else:
        formatted_date = date_filter(data.date, 'Y-m-d')
        return render(request,'edit_event.html',{'data':data,'formatted_date':formatted_date})

@login_required(login_url='signin')
def view_event(request,id):
    data = get_object_or_404(Events,id=id)
    return render(request,'view_event.html',{'data':data})

def delete_event(request,id):
    data = get_object_or_404(Events,id=id)
    data.delete()
    return redirect('dashboard')

def forget_pass(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if User.objects.filter(username=email).exists():
            if password == repassword:
                User.objects.filter(username=email).update(password=make_password(password))
                messages.success(request,'Password updated !!!',extra_tags='error')
                return redirect('signin')
            else:
                messages.error(request,'Both passwords must be same !!!',extra_tags='error')
                return redirect('forget_pass')
        else:
            messages.error(request,'Email does not exists !!!',extra_tags='error')
            return redirect('index')
    else:
        return render(request,'forget_pass.html')

@login_required(login_url='signin')
def change_pass(request):
    user = request.user
    logged = user.username
    if request.method=='POST':
        newpass = request.POST['newpass']
        oldpass = request.POST['oldpass']
        if user.check_password(oldpass):
            User.objects.filter(username=logged).update(password=make_password(newpass))
            messages.success(request,'Password updated !!!',extra_tags='success')
            logout(request)
            return redirect('signin')
        else:
            messages.error(request,'Enter correct old password !!!',extra_tags='error')
            return redirect('change_pass')
    else:
        return render(request,'change_pass.html',{'logged':logged})


# Create your views here.
