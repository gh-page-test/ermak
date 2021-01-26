from django.urls import path, include
from .views import Portfolio_view, Series_of_photos_view, Get_a_series_of_photos_starting_with_view

urlpatterns = [
    path('', Portfolio_view.as_view(), name = "portfolio" ),
    path('photoset/<int:pk>/', Series_of_photos_view.as_view(), name = "series_of_photos" ),
    path('api/series_of_photos/start=<int:start>', Get_a_series_of_photos_starting_with_view.as_view({'get': 'list'}), name = "get_a_series_of_photos_starting_with" ),
]