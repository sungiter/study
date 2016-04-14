from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Catagory(models.Model):
	catagory=models.CharField(max_length=20)

	def __unicode__(self):
		return self.catagory

class Item(models.Model):
	catagory=models.ForeignKey(Catagory)
	question=models.TextField()
	answer=models.TextField()
	created_time=models.DateTimeField(default=timezone.now)
	
	def __unicode__(self):
		return self.question
