from django.shortcuts import render
from .models import Cart, Wishlist, Compare, Checkout, Login, Account



def cart(request):
    other_pages = Cart.objects.all()
    context ={'cart': cart}
    return render(request, 'cart.html',context)

def wishlist(request):
    other_pages = Wishlist.objects.all()
    context ={'wishlist': wishlist}
    return render(request, 'wishlist.html',context)

def compare(request):
    other_pages = Compare.objects.all()
    context ={'compare': compare}
    return render(request, 'compare.html',context)

def checkout(request):
    other_pages = Checkout.objects.all()
    context ={'checkout': checkout}
    return render(request, 'checkout.html',context)


def login(request):
    other_pages = Login.objects.all()
    context ={'login': login}
    return render(request, 'login.html',context)

def account(request):
    other_pages = Account.objects.all()
    context ={'account': account}
    return render(request, 'my-account.html',context)

