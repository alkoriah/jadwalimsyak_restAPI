from rest_framework import serializers
from . models import jadwalimsak

class jadwalimsakSerializer(serializers.ModelSerializer):
	class Meta:
		model = jadwalimsak
		fields = "__all__"