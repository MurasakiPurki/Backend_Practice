from django.shortcuts import render, redirect, get_object_or_404
from .forms import createpost
from .models import Blog_post

# Create your views here.
def index(request):
    return render(request, 'index.html')

def postlist(request):
    blogs = Blog_post.objects.all()
    return render(request, 'postlist.html',{'blogs':blogs})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def editpost(request):
    if request.method == 'POST':
        
        form = createpost(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('postlist')
        
        else:
            return redirect('index')
    
    else:
        form = createpost()
        return render(request, 'editpost.html',{'form': form})

def post_detail(request, blog_id):
    blog_detail = get_object_or_404(Blog_post, pk=blog_id)
    
    return render(request, 'post_detail.html' , {'blog_detail': blog_detail})