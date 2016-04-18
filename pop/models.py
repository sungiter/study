from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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


class Master(models.Model):
	user=User()
	degree=models.TextField()


	def set_degree(self,catagory):
		if not Catagory.objects.filter(catagory=catagory):
			self.degree={}
		else:
			self.degree={catagory:{},}
			items=Items.objects.fliter(catagory_catagory=catagory)
			for item in items:
				self.degree[catagory][item.pk]=0
			
