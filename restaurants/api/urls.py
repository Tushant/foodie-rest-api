from django.conf.urls import url, include

from .views import ( RestaurantList, RestaurantDetailAPI, RestaurantCreateAPI, RestaurantUpdateAPI, RestaurantDestroyAPI,
				 MealList, MealCategoryList,)

urlpatterns = [
    url(r'^$', RestaurantList.as_view(), name="restaurantlist"),
    url(r'^(?P<slug>[\w-]+)', RestaurantDetailAPI.as_view(), name="restaurantdetail"),
    url(r'^create/$', RestaurantCreateAPI.as_view(), name="restaurantcreate"),
    url(r'^edit/(?P<slug>[\w-]+)$', RestaurantUpdateAPI.as_view(), name="restaurantedit"),
    url(r'^delete/(?P<slug>[\w-]+)$', RestaurantDestroyAPI.as_view(), name="restaurantdelete"),
    url(r'^meal/$', MealList.as_view(), name="meallist"),
    url(r'^meal-category/$', MealCategoryList.as_view(), name="mealcategorylist"),
     # url(r'^/(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
]
