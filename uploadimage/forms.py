# forms.py
from django import forms
from .models import UploadImage


class ImageForm(forms.ModelForm):

	class Meta:
		model = UploadImage
		fields = ['name', 'image_file']
