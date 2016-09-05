from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView,
									 DestroyAPIView, CreateAPIView,)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status

from oauth2_provider.models import AccessToken
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User 
from django.utils import timezone

from .serializers import ( RestaurantSerializer, RestaurantCreateUpdateSerializer, 
						MealSerializer, MealCategorySerializer, UserCreateSerializer, UserLoginSerializer,)
from restaurants.models import Restaurant, Meal, MealCategory
from .mixins import UserRestaurantMixin



class UserCreateAPI(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UserLoginAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
    	print(request.data)
    	print('access token', request.data.get('access_token'))
    	access_token = AccessToken.objects.get(token=request.data.get('access_token'), expires__gt=timezone.now())
    	data = request.data
    	serializer = UserLoginSerializer(data=data)
    	if serializer.is_valid(raise_exception=True):
    		new_data = serializer.data
    		return Response(new_data, status=status.HTTP_200_OK)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class RegistrationView(APIView):
# 	permission_classes = ()

# 	def post(self, request):
# 		serializer = RegistrationSerializer(data=request.data) # deserialized to save python native objects to db

# 		if not serializer.is_vaild():
# 			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 		data = request.data
# 		user = User.objects.create(username=data['username'])
# 		user.set_password(data['password'])
# 		user.save()

# 		# create OAuth2 Client
# 		name = user.username
# 		client = Client(user=user, name=name, url='' + name, client_id=name, client_secret='', client_type=1)
# 		client.save()
# 		return Response(serializer.data, status = HTTP_201_CREATED)

class RestaurantList(APIView):
	'list all restaurant, or create a new restaurant'
	def get(self, request, format=None):
		restaurants = RestaurantSerializer(Restaurant.objects.all().order_by('-id'), many=True).data
		return Response(restaurants)

	def post(self, request, format=None):
		serializer = RestaurantSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantCreateAPI(CreateAPIView):
	serializer_class = RestaurantCreateUpdateSerializer
	queryset = Restaurant.objects.all()
	# parser_classes = (FormParser,MultiPartParser,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class RestaurantUpdateAPI(UserRestaurantMixin, RetrieveUpdateAPIView):
	serializer_class = RestaurantCreateUpdateSerializer
	queryset = Restaurant.objects.all()
	parser_classes = (FormParser,MultiPartParser,)
	lookup_field = 'slug'

	def perform_update(self, serializer):
		print('serializer',serializer)
		instance = serializer.save()
		# send_email_confirmation(user=self.request.user, modified=instance)

class RestaurantDestroyAPI(UserRestaurantMixin, DestroyAPIView):
	serializer_class = RestaurantCreateUpdateSerializer
	queryset = Restaurant.objects.all()
	lookup_field = 'slug'

class MealList(APIView):
	def get(self, request, format=None):
		meal = MealSerializer(Meal.objects.all().order_by('-id'), many=True).data
		return Response(meal)

class MealCategoryList(APIView):
	def get(self, request, format=None):
		meal_category = MealCategorySerializer(MealCategory.objects.all().order_by('-id'), many=True).data
		return Response(meal_category)




#  ListAPIView has get_queryset

# def update(self, request, pk=None):
#         user = User.objects.filter(id=pk).first()
#         if not user or request.user != user:
#             return HttpResponseForbidden()
#         return super(UserViewSet, self).update(request)