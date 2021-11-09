from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class LandingPageView(TemplateView):
    template_name = 'user.html'

class JardinSueView(TemplateView):
    template_name = 'jardinsue.html'