from django.urls import path

from . import views

app_name = 'User'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("<int:user_id>/permission/", views.permission_request, name="permission"),
]