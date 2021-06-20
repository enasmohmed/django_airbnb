from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import Form
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView
from property.forms import PropertyBookForm, PropertyReviewForm, PropertyForm, PropertyImageFormset
from property.models import Property, PropertyReview, PropertyImages
from django_filters.views import FilterView
from .filters import PropertyFilter


class PropertyList(FilterView):
    model = Property
    paginate_by = 8   # pagination
    filterset_class = PropertyFilter  # filter
    template_name = 'property/property_list.html'


class PropertyDetail(FormMixin, DetailView):
    model = Property
    form_class = PropertyBookForm  # book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.get_object().category)[:3]
        context["property_images"] = PropertyImages.objects.filter(property=self.get_object().id)
        return context
    
    # book
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.get_form()
            if form.is_valid():
                myform = form.save(commit=False)
                myform.property = self.get_object()
                myform.user = request.user
                myform.save()
                messages.success(request, 'Your Reservation Confirmed ')

                return redirect(reverse('property:property_detail', kwargs={'slug':self.get_object().slug}))
        else:
            return redirect(reverse('accounts:signup'))


class NewProperty(CreateView):
    model = Property
    form_class = PropertyForm

    def get(self, request, *args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_formset = PropertyImageFormset()
        return self.render_to_response(self.get_context_data(
            form=form,
            image_formset=image_formset
        ))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        image_formset = PropertyImageFormset(self.request.POST, self.request.FILES)
        if form.is_valid() and image_formset.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            # messages.success(request, 'Successfully Added Your Property')

            property = Property.objects.get(id=myform.id)
            for form in image_formset:
                myform2 = form.save(commit=False)
                myform2.property = property
                myform2.save()

            return redirect(reverse('property:property_list'))


