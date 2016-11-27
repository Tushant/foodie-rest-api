from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request, 'homepage/home.html', context)

def addRestaurant(request):
    context={}
    return render(request, 'add/add-restaurant.html', context)
