from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Subject(models.Model):
	subject=models.CharField(max_length=20,unique=True)
	
	def __unicode__(self):
		return self.subject

class Category(models.Model):
	subject=models.ForeignKey(Subject)
	category=models.CharField(max_length=20)

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
	item=models.ManyToManyField('Item',related_name='item')
	score=models.PositiveSmallIntegerField(default=0)

	def __unicode__(self):
		return self.item.get().question

class Statistics(models.Model):
	user=models.OneToOneField(User)
	remembered=models.TextField()
	studying=models.CharField(max_length=200)
	new=models.CharField(max_length=200)

	def __unicode__(self):
		return unicode(self.user)	
