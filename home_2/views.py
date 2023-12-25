from django.shortcuts import render
from .models import Home_2



def home_2(request):
    home_2 = Home_2.objects.all()
    context ={'home2': home_2}
    paginate_by = 4
    return render(request, 'home_2.html',context)


