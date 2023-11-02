from django.contrib import admin
from store.models import Product
from django.http import HttpResponse


admin.site.register(Product)


def home(request):
    pass