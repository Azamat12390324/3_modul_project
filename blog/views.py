from django.shortcuts import render
from .models import Grid_sidebar, Full_width, Single_sidebar


def grid_sidebar(request):
    blog = Grid_sidebar.objects.all()
    context ={'grid_sidebar': grid_sidebar}
    return render(request, 'blog-grid-sidebar-left.html',context)

def full_width(request):
    blog= Full_width.objects.all()
    context ={'full_width': full_width}
    return render(request, 'blog-full-width.html',context)

def single_sidebar(request):
    blog = Single_sidebar.objects.all()
    context ={'single_sidebar': single_sidebar}
    return render(request, 'blog-single-sidebar-left.html',context)

