from django.urls import path
from App2.views import *

app_name='anything2'


urlpatterns=[
    path('A2_First/',A2_First,name='A1_First'),
    path('A2_Second/',A2_Second,name='A2_Second'),
]