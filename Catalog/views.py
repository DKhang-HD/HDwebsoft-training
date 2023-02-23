from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Category, Product
from .forms import CategoryCreate, ProductCreate, WorkCreate
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


# @login_required(redirect_field_name=None)
# @permission_required('Catalog.view_category')
def catalog_page(request):
    category_list = Category.objects.all()
    p = Paginator(category_list, 2)
    page = request.GET.get('page')
    category_per_page = p.get_page(page)
    return render(request, 'Catalog/library.html',
                  {'category_list': category_list, 'category_per_page': category_per_page})


def upload_category(request):
    if request.method == 'POST':
        upload_form = CategoryCreate(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{% url 'Catalog:catalog_page' %}">reload</a>""") # fix
    else:
        upload_form = CategoryCreate()
        return render(request, 'Catalog/upload_form.html', {'upload_form': upload_form})


def update_category(request, category_id):
    category_id = int(category_id)
    try:
        book = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
    category_form = CategoryCreate(request.POST or None, instance=book)
    if category_form.is_valid():
        category_form.save()
        return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
    return render(request, 'Catalog/upload_form.html', {'upload_form': category_form})


def delete_category(request, category_id):
    category_id = int(category_id)
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
    category.delete()
    return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))


def product_page(request, category_id):
    category = get_object_or_404(Category, pk=int(category_id))
    product_list = category.product_set.all()
    p = Paginator(product_list, 2)
    page = request.GET.get('page')
    product_per_page = p.get_page(page)
    return render(request, 'Catalog/shelf.html',
                  {'category': category, 'product_per_page': product_per_page})


def upload_product(request):
    if request.method == 'POST':
        upload_form = ProductCreate(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{% url 'Catalog:catalog_page' %}">reload</a>""") # fix
    else:
        upload_form = ProductCreate()
        return render(request, 'Catalog/upload_form.html', {'upload_form': upload_form})


def update_book(request, product_id):
    product_id = int(product_id)
    try:
        book = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
    product_form = ProductCreate(request.POST or None, instance=book)
    if product_form.is_valid():
        product_form.save()
        return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
    return render(request, 'Catalog/upload_form.html', {'upload_form': product_form})


def delete_book(request, product_id):
    product_id = int(product_id)
    try:
        book = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))
    book.delete()
    return HttpResponseRedirect(reverse_lazy('Catalog:catalog_page'))

