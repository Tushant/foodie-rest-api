from datetime import datetime
from datetime import timedelta

from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView,
									 DestroyAPIView, CreateAPIView,)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from oauth2_provider.models import AccessToken, Application, RefreshToken
from oauthlib.common import generate_token

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone

from .serializers import ( UserCreateSerializer, UserLoginSerializer,)
from restaurants.models import Restaurant, Meal, MealCategory


@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)

class UserCreateAPI(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UserLoginAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
    	access_token = request.GET.get('access_token')
    	data = request.data
    	print('data',data)
    	serializer = UserLoginSerializer(data=data)
    	if serializer.is_valid(raise_exception=True):
    		new_data = serializer.data
    		if new_data:
    			app = Application.objects.get(name="Foodie")
    			try:
    				user = User.objects.get(username=data['username'])
    				print ('user',user)
    			except ObjectDoesNotExist:
    				return HttpResponse("Can't find this user")
    			# else:
    			# 	try:
    			# 		old_access_token = AccessToken.objects.get(user=user, application=application)
				# 		old_refresh_token = RefreshToken.objects.get(user=user, access_token=old_access_token)
    			# 	except ObjectDoesNotExist:
    			# 		return HttpResponse('Have not set any token')
    			# 	else:
    			# 		old_access_token.delete()
    			# 		old_refresh_token.delete()
    			# new_token = generate_token()
				# refresh_token = generate_token()
    			# access_token=AccessToken.objects.create(user=user, application=app, expires=datetime.now() + timedelta(days=365),token=new_token)
				# RefreshToken.objects.create(user=user, application=app, token=refresh_token, access_token=access_token)
    			# print('aceess',AccessToken)
    			login(request, user)
    		return Response(new_data, status=status.HTTP_200_OK)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework import generics, mixins, permissions

# User = get_user_model()

# class UserIsOwnerOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.id == request.user.id

# class UserProfileChangeAPIView(generics.RetrieveAPIView,
#                                mixins.DestroyModelMixin,
#                                mixins.UpdateModelMixin):
#     permission_classes = (
#         permissions.IsAuthenticated,
#         UserIsOwnerOrReadOnly,
#     )
#     serializer_class = UserProfileChangeSerializer
#     parser_classes = (MultiPartParser, FormParser,)

#     def get_object(self):
#         username = self.kwargs["username"]
#         obj = get_object_or_404(User, username=username)
#         return obj

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
