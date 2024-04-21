from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define the URL pattern for the index view
    path('delete/<int:location_id>/', views.delete_location, name='delete_location'),
]
