from django.shortcuts import render
from .models import About_us


def about_us(request):
    about = About_us.objects.all()
    context ={'about_us': about_us}
    return render(request, 'about-us.html',context)

