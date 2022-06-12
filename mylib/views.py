from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import BookRegistration
from .models import Book
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def bookdashb(request):
    if request.method=="POST":
     fm=BookRegistration(request.POST)
     if request.POST.get('bookname') and request.POST.get('authorname'):
      
      fm.bookname=request.POST.get('bookname')
      fm.authorname=request.POST.get('authorname')
      fm.save()
      fm=BookRegistration()

    else: 
    
     fm=BookRegistration()
    libr=Book.objects.all()
     
      
    return render (request,'bookdash.html',{'form':fm,'lib':libr})

def delete_data(request,id):
  if request.method == 'POST':
    pi = Book.objects.filter(pk=id) 
    pi.delete()
  return HttpResponseRedirect('/')  


def dashboard(request):
  return render(request,'home.html')  

def update_data(request,id):
  if request.method == 'POST':
    pi = Book.objects.get(pk=id) 
    fm=BookRegistration(request.POST,instance=pi)
    if fm.is_valid():
     fm.save() 
  else:
    pi = Book.objects.get(pk=id) 
    fm=BookRegistration(instance=pi)   
  
  return render(request,'updateb.html',{'form':fm})     


def ulogin(request):
  if request.method == "POST":
   fm=AuthenticationForm(request=request,data=request.POST)
   if fm.is_valid():
    uname = fm.cleaned_data['username']
    upass = fm.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    if user is not None:
      login(request,user)
      return HttpResponseRedirect('/dash/')
  else:
    fm = AuthenticationForm()    
  return render(request,'login.html',{'form':fm})  


def signupp(request):
  if request.method == "POST":
   fm=UserCreationForm(request.POST)
   if fm.is_valid():
    fm.save()
  else:
    fm = UserCreationForm()       
  return render(request,'signup.html',{'form':fm})  



def user_profile(request):
  return render(request,'profile.html')  