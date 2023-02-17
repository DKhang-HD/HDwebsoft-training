from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
# Create your views here.

def index(request):
    category_list = Category.objects.order_by('-type_book')  
    context = {
        'category_list' : category_list,
    }
    return render(request, 'Catalog/index.html', context)

def detail(request,category_id):
    category = get_object_or_404(Category, pk = category_id)
    return render(request, 'Catalog/detail.html', {'category':category})
