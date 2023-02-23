from django import forms
from .models import StudentModel


class UploadFileForm(forms.Form):
    name_student = forms.CharField(max_length=50)
    grade_student = forms.IntegerField(min_value=1, max_value=12)
    # file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    file = forms.FileField()


class UploadFileModelForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['name', 'grade', 'file_student']
