from django.contrib import messages
from django.forms import Form
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView
from property.forms import PropertyBookForm, PropertyReviewForm
from property.models import Property, PropertyReview, PropertyImages
from django_filters.views import FilterView
from .filters import PropertyFilter


class PropertyList(FilterView):
    model = Property
    paginate_by = 6   # pagination
    filterset_class = PropertyFilter  # filter
    template_name = 'property/property_list.html'


class PropertyDetail(FormMixin, DetailView):
    model = Property
    form_class = PropertyBookForm  # book


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.get_object().category)[:3]
        context['review_count'] = PropertyReview.objects.filter(property=self.get_object()).count()
        context["property_images"] = PropertyImages.objects.filter(property=self.get_object().id)
        return context
    
    # book
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()
            messages.success(request, 'Your Reservation Confirmed ')

            return redirect(reverse('property:property_detail', kwargs={'slug':self.get_object().slug}))


class NewProperty(CreateView):
    model = Property
    fields = ['name', 'image', 'price', 'description', 'place', 'category']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            messages.success(request, 'Successfully Added Your Property')

            return redirect(reverse('property:property_list'))


