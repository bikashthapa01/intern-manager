from django import forms
from django.contrib.auth.models import User
from .models import Profile




class SuperuserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username','first_name','last_name','email')

class SuperuserProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('phone','admin_remark','stipend','date_of_joining','date_of_leaving')


class ProfileEditForm(forms.ModelForm):

	class Meta:
		model = User 
		fields = ('username','first_name','last_name','email')


class UserProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('phone','profile_image')





	