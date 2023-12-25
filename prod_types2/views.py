from django.shortcuts import render
from .models import Tab_left, Gallery_left, Sticky_left


def tab_left(request):
    product_types = Tab_left.objects.all()
    context ={'tab_left': tab_left}
    return render(request, 'pr-tab-left.html',context)

def gallery_left(request):
    product_types = Gallery_left.objects.all()
    context ={'gallery_left': gallery_left}
    return render(request, 'prod-gallery-left.html',context)

def sticky_left(request):
    product_types = Sticky_left.objects.all()
    context ={'sticky_left': sticky_left}
    return render(request, 'prod-sticky-left.html',context)

