"""blogamr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts import api

from posts.views import index, posts, about, contact, videos,pagepost
from django.urls import path



app_name= 'posts'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="main"),
    path('posts', posts),
    path('about', about),
    path('contact', contact),
    path('videos', videos),
    path('pagepost<slug:slug>',pagepost,name="pagepost"),
    path('store/',include('store.urls')),
    #api
    path('posts/api/', api.postlistapi , name='api')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

