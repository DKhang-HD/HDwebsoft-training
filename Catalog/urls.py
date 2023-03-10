from django.urls import path
from . import views


app_name = 'Catalog'
urlpatterns = [
    path('', views.catalog_page, name='catalog_page'),
    path('<int:category_id>/product/', views.product_page, name='product_page'),
    path('upload_category/', views.upload_category, name='upload_category'),
    path('update_category/<int:category_id>', views.update_category, name='update_category'),
    path('delete_category/<int:category_id>', views.delete_category, name='delete_category'),
    path('upload_product/', views.upload_product, name='upload_product'),
    path('update_product/<int:product_id>', views.update_book, name='update_product'),
    path('delete_product/<int:product_id>', views.delete_book, name='delete_product'),
]




