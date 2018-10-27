from django import forms
from . import models

class CreateMiner(forms.ModelForm):
	class Meta:
		model = models.Miner
		fields = ['name','para1','para2','para3','para4','para5']

class CreatePoolMux(forms.ModelForm):
	class Meta:
		model = models.PoolMux
		fields = ['pool', 'miner']