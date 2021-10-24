from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.Species.as_view() ,name='index'),
   
]