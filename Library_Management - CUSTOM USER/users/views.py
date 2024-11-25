from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import CustomUser

# Create your views here.

def home(request):
    return render(request,'home_page.html',{})

def admin_register(request):
    if(request.method == 'POST'):
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        email=request.POST.get('email')
        dname=request.POST.get('devname')
        pswrd=request.POST.get('password')
        cnfpswrd=request.POST.get('confpassword')
        adres=request.POST.get('address')
        phone=request.POST.get('number')
        if(pswrd == cnfpswrd):
            k = CustomUser.objects.create_user(username=dname,password=pswrd,first_name=fname,last_name=lname,email=email,address=adres,phone=phone,is_superuser=True)
            k.save()
        else:
            return HttpResponse("Passwords not matching")
        return redirect('users:user_login')
    return render(request,'admin_register.html',{})


def user_register(request):
    if(request.method == 'POST'):
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        email=request.POST.get('email')
        uname=request.POST.get('username')
        pswrd=request.POST.get('password')
        cnfpswrd=request.POST.get('confpassword')
        adres=request.POST.get('address')
        phone=request.POST.get('number')
        if(pswrd == cnfpswrd):
            k = CustomUser.objects.create_user(username=uname,password=pswrd,first_name=fname,last_name=lname,email=email,address=adres,phone=phone,is_user=True)
            k.save()
        else:
            return HttpResponse("Passwords not matching")
        return redirect('users:user_login')
    return render(request,'user_register.html',{})

def user_login(request):
    if(request.method == 'POST'):
        u=request.POST.get('u')
        p=request.POST.get('p')
        user=authenticate(username=u,password=p)
        if user and user.is_superuser == True:
            login(request, user)
            return redirect('users:home')
        if user and user.is_user == True:
            login(request, user)
            return redirect('users:home')
        else:
            return HttpResponse("Invalid User")

    return render(request,'user_login.html',{})

@login_required
def view_users(request):
    k=CustomUser.objects.all()
    return  render(request,'view_users.html',{'viewusers':k})


@login_required
def user_logout(request):
    logout(request)
    return redirect('users:user_login')



@login_required
def delete_user(request,d):
    k=CustomUser.objects.get(id=d)
    k.delete()
    return view_users(request)

@login_required
def edit_user(request,i):
    k=CustomUser.objects.get(id=i)
    if(request.method == 'POST'):
        k.usr = request.POST['usr']
        k.fname = request.POST['fname']
        k.lname = request.POST['lname']
        k.mail = request.POST['mail']
        k.adrs = request.POST['adrs']
        k.ph = request.POST['ph']
        k.ad = request.POST['ad']
        k.us = request.POST['us']
        k.save()
        return view_users(request)
    return render(request,'edit_user.html',{'user':k})
























