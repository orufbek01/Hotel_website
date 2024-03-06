from django.urls import path
from .views import index_view, room_view,about_view, contect_view

urlpatterns = [
    path('', index_view, name='index_url'),
    path('rooms/', room_view, name='rooms_url'),
    path('about/', about_view, name='about_us_url'),
    path('contact/', contect_view, name='contact_url'),
]