from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from ..forms import createpost
from ..models import Blog_post



def post_list(request):
    blogs = Blog_post.objects.all()
    return render(request, 'post_list.html',{'blogs':blogs})

@login_required(login_url='sign_in')
def post_write(request):
    if request.method == 'POST':
        
        form = createpost(request.POST)
        
        if form.is_valid():
            Blog_post = form.save()
            Blog_post.author = request.user
            Blog_post.save()

            return redirect('post_list')
        
        else:
            return redirect('post_write')
    
    else:
        form = createpost()
        return render(request, 'post_write.html',{'form': form})

def post_detail(request, blog_id):
    blog_detail = get_object_or_404(Blog_post, pk=blog_id)
    
    return render(request, 'post_detail.html' ,{'blog_detail':blog_detail})

@login_required(login_url='sign_in')
def post_edit(request, blog_id):
    blog_detail = get_object_or_404(Blog_post, pk=blog_id)
    if request.user == blog_detail.author:
        if request.method == 'POST':
            
            form = createpost(request.POST, instance=blog_detail)
        
            if form.is_valid():
                blog_detail = form.save()
                blog_detail.author = request.user
                blog_detail.pub_date = timezone.now()
                blog_detail.save()
                return render(request, 'post_detail.html' ,{'blog_detail':blog_detail})
        
            else:
                return render(request, 'post_detail.html' ,{'blog_detail':blog_detail})
    
        else:
            form = createpost(instance=blog_detail)
            return render(request, 'post_edit.html',{'form': form})
    else:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('post_detail')

@login_required(login_url='sign_in')
def post_delete(request, blog_id):
    blog_detail = get_object_or_404(Blog_post, pk=blog_id)
    if request.user == blog_detail.author:
        blog_detail.delete()
        return redirect('post_list')
    else:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('post_detail')