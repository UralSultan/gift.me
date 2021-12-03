from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class About(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	country = models.CharField(max_length=30)
	date_of_birth = models.DateField()
	email = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=15)
	image = models.ImageField("/profile_image", null=True)
	about = models.TextField()
	size_l = models.CharField(max_length=20)
	size_d = models.CharField(max_length=1)
	hobbi = models.TextField()
	important = models.TextField()

	def __str__(self):
		return self.first_name
