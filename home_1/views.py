from django.shortcuts import render
from .models import Home_1
from django.views.generic import ListView


def home_1(request):
    home_1 = Home_1.objects.all()
    context ={'home1': home_1}
    paginate_by = 4
    return render(request, 'home_1.html',context)
