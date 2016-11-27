from datetime import datetime
from datetime import timedelta
from rest_framework.serializers import (
								ModelSerializer, HyperlinkedIdentityField, HyperlinkedModelSerializer,
								SerializerMethodField, StringRelatedField, ReadOnlyField, PrimaryKeyRelatedField,
								EmailField, CharField, ValidationError,
								)

from restaurants.models import ( Restaurant, MealCategory,
								Meal, Timing, Feature,
								)

from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token
from oauth2_provider.models import AccessToken, Application, RefreshToken

from django.contrib.auth.models import User

class RegistrationSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'password',)

class FeatureSerializer(ModelSerializer):
	class Meta:
		model = Feature

class TimingSerializer(ModelSerializer):
	class Meta:
		model = Timing



class MealCategorySerializer(ModelSerializer):
	# meal = SerializerMethodField()
	class Meta:
		model = MealCategory

	# def get_meal(self, obj):
	# 	print('object of meal',obj)
	# 	instance = MealCategory.objects.get(slug=obj.slug)
	# 	meal_qs = instance.meal_set.filter(available=True)
	# 	meal = MealSerializer(meal_qs, many=True).data
	# 	return meal

class MealSerializer(ModelSerializer):
	meal_category = MealCategorySerializer(read_only=True)
	class Meta:
		model = Meal

	def get_meal_category(self, obj):
		instance = Meal.objects.get(slug=obj.slug)
		qs = instance.meal_category.all()
		print(qs)

class RestaurantSerializer(ModelSerializer):
	owner = SerializerMethodField()
	features = FeatureSerializer(many=True)
	timings = TimingSerializer(many=True)
	meal = SerializerMethodField()
	class Meta:
		model = Restaurant
		read_only = ('id',)

	def get_owner(self, obj):
		return str(obj.owner)

	def get_meal(self, obj):
		restaurant = Restaurant.objects.get(slug=str(obj.slug))
		meal_qs = restaurant.meal_set.filter(available=True)
		meal = MealSerializer(meal_qs, many=True).data
		return meal

class RestaurantCreateUpdateSerializer(ModelSerializer):
	owner = ReadOnlyField(source='owner.username')
	class Meta:
		model = Restaurant
		read_only = ('id',)
		fields = ('owner','name','address','city','phone_number','owner_email','status','website','features','timings',
					'image','facebook_page','twitter_handle','other_detail','is_parking','is_wifi',)

class RestaurantDetailSerializer(ModelSerializer):
	owner = SerializerMethodField()
	features = FeatureSerializer(many=True)
	timings = TimingSerializer(many=True)
	# meal = SerializerMethodField()
	class Meta:
		model = Restaurant
		read_only = ('id',)

	def get_owner(self, obj):
		return str(obj.owner)
