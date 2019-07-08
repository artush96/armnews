from django.urls import path

from .views import *

app_name = 'mainapp'
urlpatterns = [
    path('cookies/', test_cookie),
    path('', header, name='header'),
    path('search/', search_results, name='search'),
    path('interviews/', interviews),
    path('programs/', programs),
    path('programs/<str:slug>/', programsDetail, name='programs_detail'),
    path('broadcasts/', broadcasts, name='broadcasts'),
    path('broadcasts/<str:brod_slug>/', broadcasts, name='brod_url'),
    path('blog/', blog),
    path('blog/<str:slug>/', blogDetail, name='blog_detail'),
    path('aboutus/', aboutus),
]
