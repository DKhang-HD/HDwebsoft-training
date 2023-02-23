from django import forms
from .models import Category, Product, Work


class CategoryCreate(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductCreate(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class WorkCreate(forms.ModelForm):
    class Meta:
        model = Work
        fields = '__all__'
