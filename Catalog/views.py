from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


@login_required(redirect_field_name=None)
@permission_required('Catalog.view_category')
def catalog_page(request):

    category_list = Category.objects.order_by('-type_book')  
    context = {
        'category_list': category_list,
    }
    return render(request, 'Catalog/catalog_page.html', context)


def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'Catalog/detail.html', {'category': category})
