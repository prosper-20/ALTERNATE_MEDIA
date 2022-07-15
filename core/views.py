from django.shortcuts import render
from django.generics.views import ListView

# Create your views here.

class HomeView(ListView):
    template_name = "core/home.html"
