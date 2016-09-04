from datetime import datetime

from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models


class Restaurant(models.Model):
	OPEN = 1
	CLOSED = 2

	OPENING_STATUS = (
		(OPEN, 'open'),
		(CLOSED, 'closed'),
		)

	name = models.CharField(max_length=150, help_text="name of restaurant")
	slug = models.SlugField(max_length=150)
	owner = models.ForeignKey(User)
	address = models.CharField(max_length=150)
	city = models.CharField(max_length=80, help_text="name of city where restaurant is")
	phone_number = models.PositiveIntegerField()
	owner_email = models.EmailField()
	image = models.ImageField(upload_to='upload/restaurant/%Y/%m/%d', blank=True)
	features = models.ManyToManyField('Feature')
	timings = models.ManyToManyField('Timing')
	other_detail = models.TextField(blank=True, null=True, help_text="detail about your restaurant")
	website = models.URLField()
	status = models.IntegerField(choices=OPENING_STATUS, default=OPEN, help_text="status of your restaurant")
	facebook_page = models.URLField(max_length=200,blank=True, null=True)
	twitter_handle = models.CharField(max_length=15, blank=True, null=True)
	is_parking = models.BooleanField(default=False)
	is_wifi = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.name


class Feature(models.Model):
	BREAKFAST = 'BR'
	LAUNCH = 'LA'
	DINNER = 'DI'
	DELIVERY = 'DE'
	CAFE = 'CA'
	LUXURY = 'LU'
	NIGHT = 'NI'

	FEATURE_CHOICES = (
		(BREAKFAST, 'Breakfast'),
		(LAUNCH, 'Launch'),
		(DINNER, 'Dinner'),
		(DELIVERY, 'Delivery'),
		(CAFE, 'Cafe'),
		(LUXURY, 'Luxury Dining'),
		(NIGHT, 'Night Life'),
		)

	features = models.CharField(max_length=2, choices=FEATURE_CHOICES, default=DINNER)

	def __str__(self):
		return self.features

class Timing(models.Model):
	MONDAY = 'MO'
	TUESDAY = 'TU'
	WEDNESDAY = 'WE'
	THURSDAY = 'TH'
	FRIDAY = 'FR'
	SATURDAY = 'SA'
	SUNDAY = 'SU'

	TIMING_CHOICES = (
		(MONDAY, 'Monday'),
		(TUESDAY, 'Tuesday'),
		(WEDNESDAY, 'Wednesday'),
		(THURSDAY, 'Thursday'),
		(FRIDAY, 'Friday'),
		(SATURDAY, 'Saturday'),
		(SUNDAY, 'Sunday'),
		)
	timings = models.CharField(max_length=2, choices=TIMING_CHOICES, default=MONDAY)

	def __str__(self):
		return self.timings


class Meal(models.Model):
	restaurant = models.ForeignKey(Restaurant)
	meal_category = models.ForeignKey('MealCategory')
	name = models.CharField(max_length=120, help_text="name of the meal")
	slug = models.SlugField(max_length=120)
	price = models.IntegerField()
	quantity = models.PositiveIntegerField()
	image = models.ImageField(upload_to='upload/restaurant/meal/%Y/%m/%d', blank=True)
	rating = models.FloatField()
	available = models.BooleanField(default=True)

	def __str__(self):
		return self.name



class MealCategory(models.Model):
	name = models.CharField(max_length=80, help_text="name of the category of meal")
	slug = models.SlugField(max_length=80)

	class Meta:
		verbose_name = 'Meal Category'
		verbose_name_plural = 'Meal Categories'

	def __str__(self):
		return self.name



def create_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug
	qs = Restaurant.objects.filter(slug=slug).order_by('-id')
	if qs.exists():
		new_slug = "%s-%S" %(slug, qs.first().id)
		return create_slug(instance, slug=new_slug)
	return slug

def pre_save_slug_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

from django.db.models.signals import pre_save
pre_save.connect(pre_save_slug_receiver, sender=Restaurant)



def create_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug
	qs = Meal.objects.filter(slug=slug).order_by('-id')
	if qs.exists():
		new_slug = "%s-%S" %(slug, qs.first().id)
		return create_slug(instance, slug=new_slug)
	return slug

def pre_save_slug_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

from django.db.models.signals import pre_save
pre_save.connect(pre_save_slug_receiver, sender=Meal)