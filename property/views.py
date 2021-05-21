from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from property.models import Property


class PropertyList(ListView):
    model = Property
    paginate_by = 1
    # filter
    # pagination


class PropertyDetail(DetailView):
    model = Property
    # book

