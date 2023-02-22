from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import ImageForm
from .models import UploadImage
# Create your views here.


def imageview(request):
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse_lazy("uploadimage:success"))
	else:
		form = ImageForm()
	return render(request, 'uploadimage/upload.html', {'form': form})


def success(request):
	return HttpResponse('successfully uploaded')


# display image
def displayimages(request):
	if request.method == 'GET':
		# getting all the objects.
		images = UploadImage.objects.all()
		return render(request, 'uploadimage/display_images.html', {'images': images})
