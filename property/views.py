from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from property.forms import PropertyBookForm
from property.models import Property
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
        context["related"] = Property.objects.filter(category=self.get_object().category)[:2]
        return context
    
    # book
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()

            return redirect('/')

            
        

