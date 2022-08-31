"""hemoangola URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views  as auth_views
from client.views import home, find, about, regist, v404, perfil, login_user, logout_user, FindListView, change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('about/', about, name='url_about'),
    path('find/', find, name='url_find'),
    path('find_donors/', FindListView.as_view(template_name='find.html'), name='url_find'),
    path('regist/', regist, name='url_regist'),
    path('404/', v404, name='url_v404'),
    path('perfil/', perfil, name='url_perfil'),
    path('change_pwd/', change_password, name='url_password'),
    path('login/', login_user, name='url_login'),
    path('logout/', logout_user, name='url_logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

