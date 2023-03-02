from django import forms
from .models import Category, Product
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe


class ErrorListMsg(ErrorList):
    def __unicode__(self):
        return self.as_msg()

    def as_msg(self):
        if not self:
            return u''
        return mark_safe(u'\n'.join([u'<span class="red">%s</span>' % e for e in self]))


class MyBaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': ErrorListMsg}
        kwargs_new.update(kwargs)
        super(MyBaseModelForm, self).__init__(*args, **kwargs_new)


class CategoryCreate(MyBaseModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductCreate(MyBaseModelForm):
    class Meta:
        model = Product
        fields = '__all__'

# class DivErrorList(ErrorList):
#     def __unicode__(self):
#         return self.as_divs()
#
#     def as_divs(self):
#         if not self: return u''
#         return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="error">%s</div>' % e for e in self])


