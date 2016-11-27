from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView,
									 DestroyAPIView, CreateAPIView,)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status, filters

from oauth2_provider.models import AccessToken
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils import timezone

from .serializers import ( RestaurantSerializer, RestaurantCreateUpdateSerializer,
						MealSerializer, MealCategorySerializer,)
from restaurants.models import Restaurant, Meal, MealCategory
from .mixins import UserRestaurantMixin

class RestaurantList(ListAPIView):
	'list all restaurant, or create a new restaurant'
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('=features__features',)

class RestaurantDetailAPI(RetrieveAPIView):
	serializer_class = RestaurantSerializer
	queryset = Restaurant.objects.all()
	lookup_field = 'slug'

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
