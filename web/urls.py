

from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import  views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='About us'),
    path('contact/',views.contact,name='Contact us'),
    path('services/',views.services,name='services'),


    ]
