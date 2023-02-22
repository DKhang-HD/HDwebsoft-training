from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType

from Catalog.models import Category

# from django.contrib import messages

# Create your views here.


def homepage(request):
    list_user = User.objects.all()
    return render(request, "User/homepage.html", {"list_user": list_user})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, "Registration successful.")
            return HttpResponseRedirect(reverse_lazy("User:homepage"))
        # messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="User/register.html", context={"register_form": form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy("User:homepage"))
    form = AuthenticationForm()

    return render(request, "User/login.html", {"login_form": form})


def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("User:homepage"))


def permission_request(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    content_type = ContentType.objects.get_for_model(Category)
    permission = Permission.objects.get(
        codename='view_category',
        content_type=content_type,
    )
    user.user_permissions.add(permission)
    user = get_object_or_404(User, pk=user_id)
    if user.has_perm('Catalog.view_category'):
        notification = "sucessfully"
    else:
        notification = "fail"
    return render(request, "User/permission.html", {"notification": notification, 'my_user': user})


