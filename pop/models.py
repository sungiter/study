from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Subject(models.Model):
	subject=models.CharField(max_length=20,unique=True)
	description=models.TextField(null=True,blank=True)
	
	def __unicode__(self):
		return self.subject

class Category(models.Model):
	order=models.PositiveSmallIntegerField(default=0)
	subject=models.ForeignKey(Subject)
	category=models.CharField(max_length=20)
	description=models.TextField(null=True,blank=True)

	def __unicode__(self):
		return self.category

class Item(models.Model):
	category=models.ForeignKey(Category)
	question=models.TextField()
	answer=models.TextField()
	created_time=models.DateTimeField(default=timezone.now)
	
	def __unicode__(self):
		return unicode(self.question)


class Master(models.Model):
	user=models.ForeignKey(User)
	item=models.ForeignKey(Item)
	score=models.PositiveSmallIntegerField(default=0)

	def __unicode__(self):
		return unicode(self.item)

class Statistics(models.Model):
	user=models.OneToOneField(User)
	statistics=models.TextField()

	def __unicode__(self):
		return unicode(self.user)	
