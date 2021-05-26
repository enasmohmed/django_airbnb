from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.shortcuts import render

# Create your views here.
from blog.models import Post
from property.models import Place, Property, Category


def home(request):
    places = Place.objects.all().annotate(property_count=Count('property_place'))
    category = Category.objects.all()

    restaurant_list = Property.objects.filter(category__name='Restaurant')
    hotels_list = Property.objects.filter(category__name='Hotels')[:1]
    hotels_cable = Property.objects.filter(category__name='Hotels')[1:3]
    places_list = Property.objects.filter(category__name='	Places')
    recent_posts = Post.objects.all()[:3]

    users_count = User.objects.all().count()
    places_count = Property.objects.filter(category__name='	Places').count()
    restaurant_count = Property.objects.filter(category__name='Restaurant').count()
    hotels_count = Property.objects.filter(category__name='Hotels').count()

    return render(request, "settings/home.html", {
        'places': places,
        'category': category,
        'restaurant_list': restaurant_list,
        'hotels_list': hotels_list,
        'places_list': places_list,
        'hotels_cable': hotels_cable,
        'recent_posts': recent_posts,
        'users_count': users_count,
        'places_count': places_count,
        'restaurant_count': restaurant_count,
        'hotels_count': hotels_count
    })


def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')

    property_list = Property.objects.filter(
        Q(name__icontains=name) &
        Q(place__name__icontains=place)
    )

    return render(request,"settings/home_search.html", {'property_list': property_list})


def category_filter(request,category):
    category = Category.objects.get(name=category)
    property_list = Property.objects.filter(category=category)
    return render(request,"settings/home_search.html", {'property_list': property_list})


def contact_us(request):
    pass