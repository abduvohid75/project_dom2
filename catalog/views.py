from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


# class HomePageView(TemplateView):
#     template_name="catalog/contacts.html"