import logging

from django.shortcuts import render
from django.http import HttpResponse
from .models import Item,Category,Statistics

from bin import sheduler

def index(request):
	return HttpResponse("Hello,world. You're at the Pop index page.")

def category_list(request):
	category_list=Category.objects.all()
	context={'category_list':category_list,}
	return render(request,'pop/category_list.html',context)
	

def category(request,category):
	item_list=Item.objects.filter(category__category=category)
	context={'item_list':item_list}
	return render(request,'pop/item_list.html',context)

def detail(request):
	item=Item.objects.get()
	context={'item':item}
	return render(request,'pop/detail.html',context)

def pop(request):
	statistic=Statistics.objects.all().filter(user=request.user)
	logging.debug("statistic:",statistic)
	if not statistic:
		statistic=Statistics()
		statistic.user=request.user
	else:
		statistic=statistic[0]
	item=sheduler.chooseItem(statistic)
	return render(request,'pop/pop.html',{'item':item})
		
	
