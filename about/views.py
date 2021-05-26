from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from about.models import About, FAQ


class AboutView(ListView):
    model = FAQ
    template_name = "about/faq_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last()
        return context