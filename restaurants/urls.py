from django.conf.urls import url, include

from . import views

urlpatterns = [
    # url(r'^restaurant/', views.restaurant_list, name="restaurant_list")
    url(r'^', views.home, name="home"),
    url(r'^(?:.*)/?$', views.home),
    url(r'^addrestaurant/', views.addRestaurant, name="addrestaurant")
]
