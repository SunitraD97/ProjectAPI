"""ProjectAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from ProjectAPI.blog import views 
from rest_framework import routers 
from ProjectAPI.blog.views import BlogPostViewSet,PostViewSet,CommentViewSet


router = routers.DefaultRouter()
router.register('blog/create', views.BlogPostViewSet)
router.register('post/create', views.PostViewSet)
router.register('comment/create', views.CommentViewSet)


urlpatterns = [
    #path('',views.PostViewSet, name='post'),
    path("post/list/",views.PostViewSet, name='post_list'),
    path('post/<int:pk>/', views.PostViewSet, name='post_id'),
    
    #path('<int:pk>/comment/<int:pk>/',views.CommentViewSet, name='comment_id'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('',include('blog.urls')),
]
