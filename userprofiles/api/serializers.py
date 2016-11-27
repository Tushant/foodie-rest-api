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


class UserSerializer(ModelSerializer):
	class Meta:
		model = User


class UserCreateSerializer(ModelSerializer):
	email = EmailField()
	username =  CharField()
	first_name = CharField(required=False)
	last_name = CharField(required=False)
	password = CharField()
	confirm_password = CharField()
	class Meta:
		model = User
		fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password'
        ]
		extra_kwargs = {"password": {"write_only": True}}

	def validate(self, data):
		if not data.get('password') or not data.get('confirm_password'):
			raise ValidationError('Please enter a password and cofirm it')
		if data.get('password') != data.get('confirm_password'):
			raise ValidationError('Password must match')
		return data


	def validate_email(self, email):
		existing_email = User.objects.filter(email=email).exists()
		print('existing',existing_email)
		if existing_email:
			raise ValidationError("Someone with that email address has already registered. Was it you?")
		return email


	def create(self, validated_data):
		username = validated_data['username']
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		email = validated_data['email']
		password = validated_data['password']
		confirm_password = validated_data['password']
		user_obj = User(
		        username = username,
		        first_name = first_name,
		        last_name = last_name,
		        email = email
		    )
		user_obj.set_password(password)
		user_obj.save()
		# if user_obj:
		# 	expire_seconds = oauth2_settings.user_settings['ACCESS_TOKEN_EXPIRE_SECONDS']
		# 	scopes = oauth2_settings.user_settings['SCOPES']

		# 	application = Application.objects.get(name="Foodie")
		# 	expires = datetime.now() + timedelta(seconds=expire_seconds)
		# 	access_token = AccessToken.objects.create(user=user_obj,
		# 											application=application,
		# 											token = generate_token(),
		# 											expires=expires,
		# 											scope=scopes)
		return validated_data



class UserLoginSerializer(ModelSerializer):
    username = CharField()
    class Meta:
        model = User
        fields = [
            'username',
            # 'email',
            'password',
            # 'token',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        return data
