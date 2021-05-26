from django.urls import path

from settings import views

app_name = "settings"


urlpatterns = [
    path("", views.home, name="home"),
    path("search", views.home_search, name="home_search"),
    path("contact-us", views.contact_us, name="contact_us"),
    path("category/<slug:category>", views.category_filter, name="category_filter"),
]
