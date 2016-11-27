from django.contrib import admin

from .models import Restaurant, Meal, MealCategory, Feature, Timing

class RestaurantAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	class Meta:
		model = Restaurant
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Meal)
admin.site.register(MealCategory)
admin.site.register(Feature)
admin.site.register(Timing)