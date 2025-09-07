from django.urls import path
from .views import booking_view
from . import views

app_name = "booking"  # <-- namespace


urlpatterns = [
    path('', booking_view, name='booking'),
    #path("", views.home, name="home"),
    path("", views.booking_view, name="home"),
]
