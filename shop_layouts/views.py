from django.shortcuts import render
from .models import Grid_Left , Full_width, List_sidebar


def grid_left(request):
    shop_layouts = Grid_Left.objects.all()
    context ={'grid_left': grid_left}
    return render(request, 'shop-grid-left.html',context)

def full_width(request):
    shop_layouts = Full_width.objects.all()
    context ={'full_width': full_width}
    return render(request, 'shop-full-width.html',context)

def list_sidebar(request):
    shop_layouts = List_sidebar.objects.all()
    context ={'list_sidebar': list_sidebar}
    return render(request, 'shop-list-sidebar-left.html',context)
