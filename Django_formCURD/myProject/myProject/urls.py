
from django.contrib import admin
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', formShow),
    path('view/',view , name='view'),

    path('EditForm/<int:id>',EditForm , name='EditForm'),
    path('Delete/<int:id>',Delete , name='Delete'),
]
