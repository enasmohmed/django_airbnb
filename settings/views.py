from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Q, Count
from django.http import JsonResponse
from django.shortcuts import render

from accounts.models import Profile
from .tasks import send_mail_task
# Create your views here.
from blog.models import Post
from project import settings
from property.models import Place, Property, Category, PropertyRoomFacilities, PropertyBook, PropertyReview
from settings.models import Settings, NewsLetter, Services


def home(request):
    places = Place.objects.all().annotate(property_count=Count('property_place'))
    category = Category.objects.all()
    hotel_facilities = PropertyRoomFacilities.objects.all()

    restaurant_list = Property.objects.filter(category__name='Restaurant')
    hotels_list = Property.objects.filter(category__name='Hotels')[:1]
    hotels_cable = Property.objects.filter(category__name='Hotels')[1:3]
    places_list = Place.objects.all().annotate(property_count=Count('property_place'))[:4]
    recent_posts = Post.objects.all()[:3]

    users_count = User.objects.all().count()
    places_count = Place.objects.all().annotate(property_count=Count('property_place')).count()
    restaurant_count = Property.objects.filter(category__name='Restaurant').count()
    hotels_count = Property.objects.filter(category__name='Hotels').count()
    review_count = PropertyReview.objects.all()[:3]

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
        'hotels_count': hotels_count,
        'hotel_facilities': hotel_facilities,
        'review_count': review_count,
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
    category = Category.objects.get(id=category)
    property_list = Property.objects.filter(category=category)
    return render(request,"settings/home_search.html", {'property_list': property_list})


def contact(request):
    site_info = Settings.objects.last()

    if request.method == 'POST':
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail_task.delay(subject, name, email, message)

    return render(request,'settings/contact.html',{'site_info': site_info})


def dashboard(request):
    category = Category.objects.all()
    users_count = User.objects.all().count()
    places_count = Place.objects.all().annotate(property_count=Count('property_place')).count()
    restaurant_count = Property.objects.filter(category__name='Restaurant').count()
    hotels_count = Property.objects.filter(category__name='Hotels').count()
    posts_count = Post.objects.all().count()
    booking_count = PropertyBook.objects.all().count()
    review_count = PropertyReview.objects.all().count()
    hotel_facilities = PropertyRoomFacilities.objects.all().count()
    property = Property.objects.all()
    profile = Profile.objects.get(user=request.user)

    return render(request,'settings/dashboard.html', {
        'profile': profile,
        'property': property,
        'users_count': users_count,
        'places_count': places_count,
        'restaurant_count': restaurant_count,
        'hotels_count': hotels_count,
        'posts_count': posts_count,
        'booking_count': booking_count,
        'review_count': review_count,
        'hotel_facilities': hotel_facilities,
        'category': category
    })


def dashboard_search(request):
    name = request.GET.get('name')

    property_list = Property.objects.filter(
        Q(name__icontains=name)
    )

    return render(request,"settings/home_search.html", {'property_list': property_list})


def news_letter_subscribe(request):
    email = request.POST.get('emailInput')
    NewsLetter.objects.create(email=email)
    return JsonResponse({'done': 'done'})


def services(request):
    services = Services.objects.all()
    return render(request, 'settings/services.html', {'services': services})