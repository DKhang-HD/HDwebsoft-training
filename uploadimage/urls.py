
from django.urls import path
from . import views
app_name = "uploadimage"
urlpatterns = [
	path('', views.image_view, name='uploadimage'),
	path('success/', views.success, name='success'),
    path('images/', views.display_images, name = 'images'),
]

