from django.shortcuts import render
from shop.models import category,product
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def allcategories(request):
    c=category.objects.all()
    return render(request,'category.html',{'c':c})
def allproducts(request,p):
    c=category.objects.get(name=p)
    p=product.objects.filter(category=c)
    return render(request,'products.html',{'c':c,'p':p})
def details(request,c):
    p=product.objects.get(name=c)
    return render(request,'details.html',{'p':p})



def register(request):
    if(request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        a= request.POST['a']
        x = request.POST['x']
        z = request.POST['z']

        if(p==cp):
            user =User.objects.create_user(username=u, password=p,email=a,first_name=x,last_name=z, )
            user.save()
            return redirect('shop:allcat')
        else:
            return HttpResponse("passwords are not same")
    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return HttpResponse("invalid credentials")
    return render(request,'userlogin.html')
def user_logout(request):
    logout(request)
    return user_login(request)

