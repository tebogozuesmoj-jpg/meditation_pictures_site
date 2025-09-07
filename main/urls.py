from django.urls import path,include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    #path('book/', views.book, name='book'),
    path("booking/", include("booking.urls")),
]
