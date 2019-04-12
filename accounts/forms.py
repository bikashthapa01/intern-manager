from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class ProfileEditForm(UserChangeForm):

	class Meta:
		model = User 
		fields = ('username','first_name','last_name','email')

	