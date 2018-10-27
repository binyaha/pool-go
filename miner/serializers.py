from rest_framework import serializers
from .models import Miner

class Minerserializer(serializers.ModelSerializer):

	class Meta:
		model = Miner
		fields = '__all__'
