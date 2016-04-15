from django.shortcuts import render
from django.http import HttpResponse
from .models import Item,Catagory

def index(request):
	return HttpResponse("Hello,world. You're at the Pop index page.")

def catagory_list(request):
	catagory=Catagory.objects.all()[0].catagory
	response="Hello,world. You're at the catagory list page"+'\n'+catagory
	print response
	return HttpResponse(response)

def catagory(request):
	return HttpResponse("Hello,world. You're at the Pop catagory page.")

def item(request):
	return HttpResponse("Hello,world. You're at the Pop item page.")

def detail(request):
	return HttpResponse("Hello,world. You're at the Pop detail page.")


