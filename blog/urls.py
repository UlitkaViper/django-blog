"""djangoblog URL Configuration

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
from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('create/', CreatePost.as_view(), name='create-post'),
    path('details/<str:id>', PostDetails.as_view(), name='post-details'),
    path('update/<str:id>', UpdatePost.as_view(), name='update-or-delete'),
    # path('update/', UpdatePost.as_view(), name='update'),

]
