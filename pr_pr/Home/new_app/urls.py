from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='new_app'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact')
]