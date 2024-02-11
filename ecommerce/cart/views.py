from django.shortcuts import render
from shop.models import product
from cart.models import Cart


# Create your views here.

def cartview(request):
    u=request.user
    cart=Cart.objects.filter(user=u)
    return render(request,'cartview.html',{'c':cart})
def addtocart(request,n):
    p=product.objects.get(name=n)
    u=request.user
    try:
        cart=Cart.filter(user=u,product=p)
        if(cart.quantity<cart.product.stock):
            cart.quantity+=1
            cart.save()
    except:
        if(p.stock >0):
            cart=Cart.objects.create(product=p,user=u,quantity=1)
            cart.save()
    return cartview(request)

def cart_remove(request,n):
    p = product.objects.get(name=n)
    u = request.user
    try:
        cart = Cart.filter(user=u, product=p)
        if (cart.quantity>1):
            cart.quantity-= 1
            cart.save()
        else:
            cart.delete()
    except:
        pass
    return cartview(request)
