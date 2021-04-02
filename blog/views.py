from django.shortcuts import render, redirect
from .forms import createpost

# Create your views here.
def index(request):
    return render(request, 'index.html')

def postlist(request):
    return render(request, 'postlist.html')

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

def samplepost(request):
    return render(request, 'samplepost.html')