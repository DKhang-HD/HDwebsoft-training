from django.urls import path

from . import views
app_name = 'uploadfile'
urlpatterns = [
    path('', views.index, name='index'),
    path('listfile/',views.upload_file, name = 'listfile'),
    path('results/',views.results, name = 'results'),
    path('success/',views.success, name = 'success'),
    path('<int:student_id>/contents/',views.contents, name = 'contents'),
]