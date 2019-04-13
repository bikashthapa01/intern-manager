from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from accounts.forms import ProfileEditForm,UserProfileEditForm

# Create your views here.

def homeView(request):
	return render(request,'accounts/home.html',{})


def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('account_home')
	else:
		form = UserCreationForm()

	return render(request,'accounts/register.html',{'form':form})

@login_required
def dashboard(request):
	return render(request,'accounts/dashboard.html',{'interns':User.objects.filter(is_staff = False).order_by('-date_joined')})

def logout(request):
	auth_logout(request)
	return redirect('account_home')

def profile(request,username):
	return render(request,'profile/profile.html',{})

def edit_profile(request,username):
	if request.method == "POST":
		form = ProfileEditForm(request.POST,instance=request.user)
		profile_form = UserProfileEditForm(request.POST, instance = request.user.profile)
		if form.is_valid() and profile_form.is_valid():
			form.save()
			profile_form.save()
			return redirect('account_profile',username=username)
	else:
		form = ProfileEditForm(instance=request.user)
		profile_form = UserProfileEditForm(instance = request.user.profile)
	return render(request,'profile/edit_profile.html',{'form':form,'profile':profile_form})