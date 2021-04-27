"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.index, name='index'),
    path('postlist/',blog.views.post_list, name='post_list'),
    path('signup/', blog.views.sign_up, name='sign_up'),
    path('signin/', blog.views.sign_in, name='sign_in'),
    path('about/', blog.views.about, name='about'),
    path('writepost/', blog.views.post_write, name='post_write'),
    path('postlist/detail/<int:blog_id>/', blog.views.post_detail, name='post_detail'),
    path('postlist/detail/<int:blog_id>/edit/', blog.views.post_edit, name='post_edit'),
    path('postlist/detail/<int:blog_id>/delete/', blog.views.post_delete, name='post_delete'),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('oauth/', blog.views.oauth, name='oauth'),
    path('kakao_sign_up/', blog.views.kakao_sign_up, name='kakao_sign_up'),
    path('logout/', blog.views.logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)