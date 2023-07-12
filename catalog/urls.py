from django.urls import path

from catalog.views import *

app_name = 'catalog'

urlpatterns = [
    path('', home, name="home_page"),
    path('contacts/', contacts, name="contacts_page"),

]
