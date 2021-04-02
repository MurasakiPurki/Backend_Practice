from django import forms
from .models import Blog_post

class createpost(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = ['title','pub_date','content','name','password']