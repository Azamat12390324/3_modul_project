from django.shortcuts import render
from .models import Contact_us


def contact_us(request):
    contact = Contact_us.objects.all()
    context ={'contact_us': contact_us}
    return render(request, 'contact-us.html',context)



