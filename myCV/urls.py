from django.urls import path
from .views import index, redirect_urls
from .views import contact


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('<slug>/', redirect_urls, name='redirect_urls'),
]

