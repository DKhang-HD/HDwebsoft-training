from django import forms
from .models import Category, Product, Order


class CategoryCreate(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductCreate(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderCreate(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
