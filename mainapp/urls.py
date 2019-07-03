from django.urls import path

from .views import *

urlpatterns = [
    path('cookies/', test_cookie),
    path('', header),
    path('interviews/', interviews),
    path('programs/', programs),
]
