from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	phone = models.IntegerField(default=0)
	stipend = models.IntegerField(default=0)
	admin_remark = models.CharField(max_length=500,default="")
	profile_image = models.ImageField(upload_to="profile_image/")
	offer_letter = models.FileField(upload_to="uploads/")
	date_of_joining = models.DateField(default=date.today())
	date_of_leaving = models.DateField(default=date.today())

	def __str__(self):
		return self.user.username

	def create_profile(sender,**kwargs):
		if kwargs['created']:
			user_profile = Profile.objects.create(user=kwargs['instance'])

	post_save.connect(create_profile,sender=User)






