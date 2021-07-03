from django.db import models
from django.db.models import query
from django.shortcuts import render
from django.views.generic import TemplateView
from catalog.models import Product

# Create your views here.

def HomePageView(request):
    products = Product.objects.all().filter(is_available=True)
    print(">>>>", products)

    context = {
        'products': products,
    }
    print("context", context)

    return render(request, 'home.html', context)
    


class AboutPageView(TemplateView):
    template_name = 'about.html'
