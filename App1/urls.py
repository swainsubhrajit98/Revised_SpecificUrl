from django.urls import path
from App1.views import *
app_name='anithing'


urlpatterns=[
    path('A1_First/',A1_First,name='A1_First'),
    path('A1_Second/',A1_Second,name='A1_Second'),
]