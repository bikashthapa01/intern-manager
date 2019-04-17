from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout,login as user_login
from django.contrib.auth.models import User
from accounts.forms import ProfileEditForm,UserProfileEditForm,SuperuserEditForm,SuperuserProfileEditForm

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
	if request.user.is_staff:
		return render(request,'accounts/dashboard.html',{'interns':User.objects.filter(is_staff = False).order_by('-date_joined')[:3],'total_interns':User.objects.filter(is_staff = False).count()})
	else:
		return redirect('account_profile',username=request.user.username)
	

def logout(request):
	auth_logout(request)
	return redirect('account_home')

@login_required
def profile(request,username):
	return render(request,'profile/profile.html',{'userdata':User.objects.get(username=username)})

@login_required
def edit_profile(request,username):
	if request.method == "POST":
		form = ProfileEditForm(request.POST,instance=request.user)
		profile_form = UserProfileEditForm(request.POST, request.FILES,instance = request.user.profile)
		if form.is_valid() and profile_form.is_valid():
			form.save()
			profile_form.save()
			return redirect('account_profile',username=username)
	else:
		form = ProfileEditForm(instance=request.user)
		profile_form = UserProfileEditForm(instance = request.user.profile)
	return render(request,'profile/edit_profile.html',{'form':form,'profile':profile_form})

@staff_member_required
def superProfileEdit(request,username):
	userdata = User.objects.get(username=username)
	
	if request.method == "POST":
		form = SuperuserEditForm(request.POST,instance=userdata)
		profile_form = SuperuserProfileEditForm(request.POST, instance = userdata.profile)
		if form.is_valid() and profile_form.is_valid():
			form.save()
			profile_form.save()
			return redirect('account_profile',username=username)
	else:
		form = SuperuserEditForm(instance=userdata)
		profile_form = SuperuserProfileEditForm(instance = userdata.profile)
	return render(request,'profile/super_edit_profile.html',{'form':form,'profile':profile_form})



@staff_member_required
def allInterns(request):
	return render(request,'accounts/interns.html',{'interns':User.objects.filter(is_staff = False).order_by('-date_joined')})