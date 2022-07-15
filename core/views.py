from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

# class HomeView(ListView):
#     template_name = "core/home.html"


def HomeView(request):
    return render(request, 'core/home.html')
