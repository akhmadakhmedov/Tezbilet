from django.urls import path
from .views import *

app_name = 'kassa'

urlpatterns = [
    path('privacy/', privacy, name='privacy'),
    path('refund/', refund, name='refund'),

]