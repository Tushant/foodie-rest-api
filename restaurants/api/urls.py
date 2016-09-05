from django.conf.urls import url, include

from .views import ( RestaurantList, RestaurantCreateAPI, RestaurantUpdateAPI, RestaurantDestroyAPI,
				 MealList, MealCategoryList, UserCreateAPI, UserLoginAPI)

urlpatterns = [
    url(r'^$', RestaurantList.as_view(), name="restaurantlist"),
    url(r'^create/$', RestaurantCreateAPI.as_view(), name="restaurantcreate"),
    url(r'^edit/(?P<slug>[\w-]+)$', RestaurantUpdateAPI.as_view(), name="restaurantcreate"),
    url(r'^delete/(?P<slug>[\w-]+)$', RestaurantDestroyAPI.as_view(), name="restaurantcreate"),
    url(r'^meal/$', MealList.as_view(), name="meallist"),
    url(r'^meal-category/$', MealCategoryList.as_view(), name="mealcategorylist"),
    url(r'^register/$', UserCreateAPI.as_view()),
    url(r'^login/$', UserLoginAPI.as_view()),
     # url(r'^/(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
]