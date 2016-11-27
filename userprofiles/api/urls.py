from django.conf.urls import url, include

from .views import ( UserCreateAPI, UserLoginAPI, secret_page )

urlpatterns = [
    url(r'^register/$', UserCreateAPI.as_view()),
    url(r'^login/$', UserLoginAPI.as_view()),
    url(r'^secret$', secret_page, name='secret'),
]
