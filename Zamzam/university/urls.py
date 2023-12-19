from django.urls import path
from .views import *

app_name = 'university'

urlpatterns = [
    path('create/', about, name='about'),
]