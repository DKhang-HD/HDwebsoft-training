from django.urls import path
from . import views

app_name = 'Catalog'

urlpatterns = [
    path('', views.catalog_page, name='catalog_page'),
    path('<int:category_id>/', views.detail, name='detail'),
]
