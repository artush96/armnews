from django.urls import path

from .views import *

app_name = 'mainapp'
urlpatterns = [
    path('cookies/', test_cookie),
    path('', header),
    path('interviews/', interviews),
    path('programs/', programs),
    path('broadcasts/', broadcasts, name='broadcasts'),
    path('broadcasts/<str:brod_slug>/', broadcasts, name='brod_url'),
    path('blog/', blog),
    path('aboutus/', aboutus)
]
