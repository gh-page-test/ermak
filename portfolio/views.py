from django.shortcuts import render

from django.views.generic import ListView, DetailView, View

from .models import Series_of_photos
from carousel.models import ImageList

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import SerieOfPhotosSerializer

class Portfolio_view(ListView):
	queryset = Series_of_photos.objects.all()[:9]
	context_object_name = 'series_of_photos'

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context["carousel"] = ImageList.objects.get()
	    return context

class Series_of_photos_view(DetailView):
	model = Series_of_photos
	context_object_name = 'series_of_photos'

class Get_a_series_of_photos_starting_with_view(viewsets.ViewSet):
    def list(self, request, start):
        queryset = Series_of_photos.objects.all()[start:start+9]
        serializer = SerieOfPhotosSerializer(queryset, many=True)
        return Response(serializer.data)