from django.shortcuts import render
from .models import  Servise, Frequently, Privacy_Policy, Page_404


def servise(request):
    pages = Servise.objects.all()
    context ={'servise': servise}
    return render(request, 'service.html',context)

def frequently(request):
    pages = Frequently.objects.all()
    context ={'frequently': frequently}
    return render(request, 'faq.html',context)
    

def privacy_policy(request):
    pages = Privacy_Policy.objects.all()
    context ={'privacy_policy': privacy_policy}
    return render(request, 'privacy-policy.html',context)

def page_404(request):
    pages = Page_404.objects.all()
    context ={'page_404': page_404}
    return render(request, '404.html',context)


