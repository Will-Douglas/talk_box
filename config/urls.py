"""config URL Configuration

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
from django.urls import path
from authentication import views
from nu_talker import views as nu_view
from posts import views as tlk_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', nu_view.index, name="Homepage"),
    path('login/', views.LoginView, name="Login"),
    path('logout/', views.TalkLogOut, name="Logout"),
    path('signup/', views.SignUpView, name="Signup"),
    path('posts/<int:post_id>/', tlk_view.talk_view, name="Talking"),
    path('talker_page/<int:user_id>/', nu_view.profile, name="Profile"),
]
