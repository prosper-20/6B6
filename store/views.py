from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm


def homepage(request):
    # return HttpResponse("<h1>Home Page</h1>")
    return render(request, "store/index.html")
    # return render(request, response)



