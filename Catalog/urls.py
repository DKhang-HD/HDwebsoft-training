from django.urls import path
from . import views

app_name = 'Catalog'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:category_id>/', views.detail, name = 'detail'),
]