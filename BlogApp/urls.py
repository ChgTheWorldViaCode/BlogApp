"""BlogApp URL Configuration

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
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 127.0.0.1:8000/accounts/login - local
    # mydjangosite.com/accounts/login - online
    path('accounts/login/', LoginView.as_view(), name='login'),
    #path('accounts/login/', auth_views.LoginView.as_view(), name='login'), 

    # 127.0.0.1:8000/accounts/logout - local
    # mydjangosite.com/accounts/logout - online
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    #path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page': 'post_list'}),     

    path('',include('blog.urls'))
]
