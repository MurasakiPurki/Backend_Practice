from django.shortcuts import render

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
    return render(request, 'editpost.html')

def samplepost(request):
    return render(request, 'samplepost.html')