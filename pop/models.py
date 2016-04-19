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
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	degree=models.TextField()


	def set_degree(self,catagory):
		if not Catagory.objects.filter(catagory=catagory):
			self.degree={}
		else:
			self.degree={catagory:{},}
			new=self.degree[catagory]['new']={}
			hover=self.degree[catagory]['hover']={}
			familiar=self.degerr[catagory]['familiar']={}
			items=Items.objects.fliter(catagory_catagory=catagory)
			for item in items:
				new[item.pk]=0
			
		
	def del(self,pk):
		if not Item.objects.filter(pk=pk):
			print("itme %d is not exits"%pk)
		else:
			item=Item.objects.get(pk=pk)
			catagory=item.catagory.catagory
			del self.degree[catagory][pk]
		

	def add(self,pk):
		if not Item.objects.filter(pk=pk):
			print("item %d is not add in the databases")
		else:
			item=Item.objects.get(pk=pk)
			catagory=item.catagory.catagory
			self.degree[catagory][pk]=0
		

	
			
