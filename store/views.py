from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product

def homepage(request):
    all_products = Product.objects.all()
    context = {"all_products": all_products}
    return render(request, "store/index.html", context)


def detailpage(request, input_id):
    current_product = Product.objects.get(id=input_id)
    context = {"current_product": current_product}
    return render(request, "store/detail.html", context)








