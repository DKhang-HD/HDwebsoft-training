
from django.urls import path
from . import views

app_name = "uploadimage"
urlpatterns = [
    path('', views.imageview, name='upload_image'),
    path('success/', views.success, name='success'),
    path('images/', views.displayimages, name='images'),
]
