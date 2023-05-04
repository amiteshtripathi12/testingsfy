from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.

# class CustomUser(AbstractUser):
#     is_doctor = models.BooleanField('Is Company', default=False)
#     is_patient = models.BooleanField('Is Patient', default=False)
#     is_admin = models.BooleanField('Is Admin', default=False)

class Slider_banner(models.Model):
	name  = models.CharField(max_length=50)
	image = models.ImageField(upload_to='home/Slider_banner')
	title = models.CharField(max_length=40,null=True,blank=True)
	text = models.CharField(max_length=100,null=True,blank=True)
	button_url = models.CharField(max_length=25, null=True,blank=True)
	button_name = models.CharField(max_length=30,null=True,blank=True)

	def __str__(self):
		return (self.name)
	
class Services(models.Model):
	name = models.CharField(max_length=20, null=True,blank=True)
	content = models.CharField(max_length=200, null=True,blank=True)
	image = models.ImageField(upload_to='home/service')
	heading = models.CharField(max_length=40, null=True,blank=True)
	subcontent = models.CharField(max_length=200, null=True,blank=True)

	def __str__(self):
		return (self.name)

class Service(models.Model):
	desc = models.CharField(max_length=250)

	def __str__(self):
		return (self.desc)

class mission_vision(models.Model):
	name = models.CharField(max_length=20)
	mission = models.CharField(max_length=500,null=True,blank=True)
	vision = models.CharField(max_length=500, null=True,blank=True)
	why_choose_us = models.CharField(max_length=500,null=True,blank=True)

	def __str__(self):
		return (self.name)

class Session_types(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='home/Session_types')
	url = models.CharField(max_length=50, default='#')

	def __str__(self):
		return (self.name)

class About_us(models.Model):
	srno = models.CharField(max_length=10, null=True,blank=True)
	content = models.CharField(max_length=1500)
	image = models.ImageField(upload_to='about_us')

	def __str__(self):
		return (self.srno)

class ContactForm(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True)
	address = models.CharField(max_length=100,null=True,blank=True)
	mobile_number = models.CharField(max_length=20,null=True,blank=True)
	Message = models.TextField(null=True,blank=True)

	def __str__(self):
		return (self.name)