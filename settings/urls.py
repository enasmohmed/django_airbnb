from django.urls import path

from settings import views

app_name = "settings"


urlpatterns = [
    path("", views.home, name="home"),
    path("search", views.home_search, name="home_search"),
    path("contact", views.contact, name="contact"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("category/<slug:category>", views.category_filter, name="category_filter"),
]
