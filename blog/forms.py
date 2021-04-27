from django import forms
from .models import Blog_post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class createpost(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = ['title','content']

        widgets = {
        
            'title':forms.TextInput(
                attrs={'class':'form-control', 'style':'width: 100%', 'placeholder':'Title'}
            ),
            'content':forms.CharField(widget=CKEditorUploadingWidget()),
        }

class BlogCommnentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['comment_textfield']
        widgets = {
            'comment_textfield': forms.Textarea(attrs={'class':'form-control','rows':4, 'cols': 40})
        }