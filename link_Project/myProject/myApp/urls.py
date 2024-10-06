from django.urls import path
from .views import home,myApp

urlpatterns = [
    path('',home),
    path('t/',myApp),
]
