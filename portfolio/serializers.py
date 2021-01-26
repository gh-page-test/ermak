from rest_framework import serializers
from .models import Series_of_photos, Photomodel

class SerieOfPhotosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Series_of_photos
		fields = ('pk', 'title', 'cover', 'city', 'date')