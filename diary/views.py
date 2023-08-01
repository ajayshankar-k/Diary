from django.shortcuts import render,redirect,get_object_or_404
from datetime import date

def index(request):
    return render(request,'index.html')
def signin(request):
    return render(request,'signin.html')
def dashboard(request):
    return render(request,'dashboard.html')
def add_event(request):
    current_date = date.today()  
    formatted_date = current_date.strftime('%Y-%m-%d')

    return render(request,'add_event.html',{'formatted_date':formatted_date})
def edit_event(request):
    return render(request,'edit_event.html')
def view_event(request):
    return render(request,'view_event.html')
def forget_pass(request):
    return render(request,'forget_pass.html')


# Create your views here.
