from django.shortcuts import render
from .models import Default, Variable,  Referral, Group, Slider


def default(request):
    product_types = Default.objects.all()
    context ={'default': default}
    return render(request, 'product-default.html',context)

def variable(request):
    product_types = Variable.objects.all()
    context ={'variable': variable}
    return render(request, 'prod-variable.html',context)

def referral(request):
    product_types = Referral.objects.all()
    context ={'referral': referral}
    return render(request, 'prod-affiliate.html',context)

def group(request):
    product_types = Group.objects.all()
    context ={'group': group}
    return render(request, 'prod-group.html',context)


def slider(request):
    product_types = Slider.objects.all()
    context ={'slider': slider}
    return render(request, 'pro-single-slide.html',context)

