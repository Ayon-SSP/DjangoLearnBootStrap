from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('docs', views.docs, name='docs' ),
    path('about', views.about, name='about' ),
    path('services', views.services, name='services' ),
    path('contact', views.contact, name='contact' ),
    path('profile', views.profile, name='profile' ),
    path('bsLearning', views.bsLearning, name='bsLearning' ),
]
