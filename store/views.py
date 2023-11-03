from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
from django.core.cache import cache
from django.generic.v

def homepage(request):
    all_products = Product.objects.all()
    context = {"all_products": all_products}
    return render(request, "store/index.html", context)


def detailpage(request, input_id):
    current_product = Product.objects.get(id=input_id)
    context = {"current_product": current_product}
    return render(request, "store/detail.html", context)



def createproductpage(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return HttpResponse("Something went wrong")
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, "store/create_product.html", context)








