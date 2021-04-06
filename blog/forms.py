from django import forms
from .models import Blog_post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class createpost(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = ['title','content','author']

        widgets = {
        
            'title':forms.TextInput(
                attrs={'class':'form-control', 'style':'width: 100%', 'placeholder':'Title'}
            ),
            'author':forms.Select(
                attrs={'class': 'custom-select'},
            ),
            'body':forms.CharField(widget=CKEditorUploadingWidget()),
        }