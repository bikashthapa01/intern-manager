"""internshipManager URL Configuration

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
from accounts.views import homeView,profile,edit_profile

urlpatterns = [
	path('',homeView,name="account_home"),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('profile/<username>/',profile,name="account_dashboard"),
    path('profile/<username>/edit/',edit_profile,name="edit_profile"),
]
