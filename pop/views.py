from django.shortcuts import render
from django.http import HttpResponse
from .models import Item,Catagory

def index(request):
	return HttpResponse("Hello,world. You're at the Pop index page.")

def catagory_list(request):
	catagory_list=Catagory.objects.all()
	context={'catagory_list':catagory_list,}
	return render(request,'pop/catagory_list.html',context)
	

def catagory(request,catagory):
	item_list=Item.objects.filter(catagory__catagory=catagory)
	context={'item_list':item_list}
	return render(request,'pop/item_list.html',context)

def detail(request,catagory,pk):
	item=Item.objects.filter(catagory__catagory=catagory).get(pk=pk)
	context={'item':item}
	return render(request,'pop/detail.html',context)


