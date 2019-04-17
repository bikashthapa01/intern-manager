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
from accounts.views import homeView,profile,edit_profile,dashboard,superProfileEdit,allInterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',homeView,name="account_home"),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('profile/<username>/',profile,name="account_profile"),
    path('profile/<username>/edit/',edit_profile,name="edit_profile"),
    path('dashboard/',dashboard,name="account_dashboard"),
    path('admin/edit/<username>/',superProfileEdit,name="admin_profile_edit"),
    path('admin/interns/',allInterns,name="all_interns")
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
