from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
from django.core.cache import cache
from django.views.generic import View

def homepage(request):
    all_products = Product.objects.all()
    context = {"all_products": all_products}
    return render(request, "store/index.html", context)

class detailpage(View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get("input_id")
        if cache.get(product_id):
            current_product = cache.get(product_id)
            print("hit the cache")
        else:
            try:
                current_product = Product.objects.get(id=product_id)
                cache.set(product_id, current_product)
                print("hit the db")
            except Product.DoesNotExist:
                return HttpResponse("This product doesn't exist")
            
        context = {"current_product": current_product}

        return render(request, "store/detail.html", context)




# def detailpage(request, input_id):
#     current_product = Product.objects.get(id=input_id)
#     context = {"current_product": current_product}
#     return render(request, "store/detail.html", context)



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








