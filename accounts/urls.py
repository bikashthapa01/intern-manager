from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
	path('login/',LoginView.as_view(),name="account_login"),
	path('logout/',views.logout,name="account_logout"),
	path('register/',views.register,name="account_register"),
	
] 