from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import createpost, BlogCommnentForm
from .models import Blog_post, Comment
import requests

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        if request.POST["password"] == request.POST["cfr_password"]:
            user = User.objects.create_user( username = request.POST["username"], password = request.POST["password"])
            auth.login(request,user)
            return redirect('index')
        else: 
            return render(request, 'signup.html')
    
    else:
        return render(request, 'signup.html')

def kakao_sign_up(request):
    
    request_uri = 'https://kauth.kakao.com/oauth/authorize?'
    client_id = 'b85bf429c9beae5b40c7faa998107542'
    redirect_uri = 'http://127.0.0.1:8000/oauth'

    request_uri += 'client_id='+client_id
    request_uri += '&redirect_uri='+redirect_uri
    request_uri += '&response_type=code'

    request.session['client_id'] = client_id
    request.session['redirect_uri'] = redirect_uri

    return redirect(request_uri)

def sign_in(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('index')



def index(request):
    return render(request, 'index.html')

def postlist(request):
    blogs = Blog_post.objects.all()
    return render(request, 'postlist.html',{'blogs':blogs})


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
    
    return render(request, 'post_detail.html' ,{'blog_detail':blog_detail})
    

def oauth(request):
    code = request.GET['code']
    print('code = '+ str(code))
    
    client_id = request.session.get('client_id')
    redirect_uri = request.session.get('redirect_uri')

    access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
    
    access_token_request_uri += "client_id=" + client_id
    access_token_request_uri += "&redirect_uri=" + redirect_uri
    access_token_request_uri += "&code=" + code

    print(access_token_request_uri)

    access_token_request_uri_data = requests.get(access_token_request_uri)
    json_data = access_token_request_uri_data.json()
    access_token = json_data['access_token']
    print(access_token)

    user_profile_uri = "https://kapi.kakao.com/v1/api/talk/profile?access_token="
    user_profile_uri += str(access_token)
    
    print(user_profile_uri)
    user_profile_uri_data = requests.get(user_profile_uri)
    user_json_data = user_profile_uri_data.json()
    nickName = user_json_data['nickName']
    profileImageURL = user_json_data['profileImageURL']
    thumbnailURL = user_json_data['thumbnailURL']

    print("nickName = "+ str(nickName))
    print("profileImageURL = "+ str(profileImageURL))
    print("thumbnailURL = " + str(thumbnailURL))
    
    if User.objects.filter(username=nickName).exists():
        username = nickName
        password = profileImageURL
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'signin.html')
    else:
        user = User.objects.create_user(username = nickName, password = profileImageURL)
        auth.login(request,user)
    
    return redirect('index')