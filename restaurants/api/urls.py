from django.conf.urls import url, include

from .views import RestaurantList, RestaurantCreateAPI, MealList, MealCategoryList

urlpatterns = [
    url(r'^$', RestaurantList.as_view(), name="restaurantlist"),
    url(r'^create/$', RestaurantCreateAPI.as_view(), name="restaurantcreate"),
    url(r'^edit/(?P<slug>[\w-]+)$', RestaurantCreateAPI.as_view(), name="restaurantcreate"),
    url(r'^delete/(?P<slug>[-w]+)$', RestaurantCreateAPI.as_view(), name="restaurantcreate"),
    url(r'^meal/$', MealList.as_view(), name="meallist"),
    url(r'^meal-category/$', MealCategoryList.as_view(), name="mealcategorylist"),
]