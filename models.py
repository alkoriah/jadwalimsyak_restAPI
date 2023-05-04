from django.db import models

# Create your models here.
class jadwalimsak (models.Model):
	Tanggal = models.CharField(max_length=50)
	Imsak 	= models.TimeField(auto_created=False)
	Subuh	= models.TimeField(auto_created=False)
	Terbit 	= models.TimeField(auto_created=False)
	Duha 	= models.TimeField(auto_created=False)
	Zuhur 	= models.TimeField(auto_created=False)
	Asar 	= models.TimeField(auto_created=False)
	Magrib 	= models.TimeField(auto_created=False)
	Isya 	= models.TimeField(auto_created=False)


	def __str__(self):
		return self.Tanggal
