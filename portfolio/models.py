# -*- coding: utf-8 -*-

from django.utils.html import format_html
from django.db import models

from imagekit.models import ImageSpecField

class Photo(models.Model):
	"""Model describing a photo"""
	photo = models.ImageField(verbose_name="фото", upload_to="photos", default=None)
	photo_webp = ImageSpecField(source='photo',
								format='WEBP',
								options={'quality': 75}
    )
	series_of_photos = models.ForeignKey(
		'Series_of_photos', verbose_name="серия фотографий", 
		on_delete=models.CASCADE, default=None,
		related_name="photos"
	)

	class Meta:
		verbose_name = "фото"
		verbose_name_plural = "фото"

	def __str__(self):
		return f'{self.photo}'

class Series_of_photos(models.Model):
	"""Model describing a series of photos"""
	title = models.CharField(verbose_name="заголовок", max_length=64, unique=True)
	cover = models.ImageField(verbose_name="обложка для серии фото", upload_to="covers", default=None)
	cover_webp = ImageSpecField(source='cover',
								format='WEBP',
								options={'quality': 75}
    )
	description = models.CharField(verbose_name="описание для серии фото", max_length=128, blank=True)
	photomodels = models.ManyToManyField(
		'Photomodel', 
		verbose_name="модели принимавшие участие в съемках"
	)
	audio = models.ForeignKey(
		'Audio', verbose_name="аудиозапись", 
		on_delete=models.SET_NULL, null=True, 
		blank=True, default=None
	)
	city = models.CharField(verbose_name="город", default="Донецк", max_length=18)
	date = models.DateField(verbose_name="дата съемок")

	class Meta:
		verbose_name = "серию фотографий"
		verbose_name_plural = "серии фотографий"

		ordering = ['-pk']

	def get_cover_img(self):
		return format_html(
			'<img style="margin: auto; max-width:150px; max-height:100px;" src="{}"/>', 
			self.cover.url
		)

	get_cover_img.short_description = "обложка"	

	def __str__(self):
		return f'{self.title}'

class Photomodel(models.Model):
	"""Model describing a photomodel"""
	name = models.CharField(verbose_name="имя фотомодели", max_length=64)
	link = models.CharField(verbose_name="ссылка на страницу фотомодели", max_length=128, default="#")

	class Meta:
		verbose_name = "фотомодель"
		verbose_name_plural = "фотомодели"

		ordering = ['name']

	def __str__(self):
		return f'{self.name}'


class Audio(models.Model):

	name = models.CharField(verbose_name="название трека", max_length=32)
	file = models.FileField(verbose_name="аудиофайл", upload_to="audio")

	class Meta:
		verbose_name = "аудиофайл"
		verbose_name_plural = "аудиофайлы"

		ordering = ['-name']
	
	def __str__(self):
		return f'{self.name}'