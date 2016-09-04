from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView,
									 DestroyAPIView, CreateAPIView,)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import RestaurantSerializer, RestaurantCreateUpdateSerializer, MealSerializer, MealCategorySerializer
from restaurants.models import Restaurant, Meal, MealCategory

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

class RestaurantUpdateAPI(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateUpdateSerializer

	def perform_update(self, serializer):
		print('serializer',serializer)
		instance = serializer.save()
		# send_email_confirmation(user=self.request.user, modified=instance)

class RestaurantDestroyAPI(DestroyAPIView):
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