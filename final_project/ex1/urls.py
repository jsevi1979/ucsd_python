from django.urls import path
from ex1 import views

urlpatterns = [

    path('', views.home),
    path('form', views.index),
    path('add', views.add),
    path('display', views.show),
    path('introduction', views.introduction),
    path('about', views.about)
]