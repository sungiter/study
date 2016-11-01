import json

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Subject,Item,Category,Statistics,Master

from bin import sheduler

def index(request):
	return HttpResponse("Hello,world. You're at the Pop index page.")

def subject(request):
	subjectList=Subject.objects.all()
	context={'subjectList':subjectList}
	return render(request,'pop/subject.html',context)
	

def category(request,category):
	item_list=Item.objects.filter(category__category=category)
	context={'item_list':item_list}
	return render(request,'pop/item_list.html',context)

def detail(request,pk):
	item=Item.objects.get(pk=pk)
	context={'item':item}
	print context
	return render(request,'pop/detail.html',context)

def pop(request,subject):
	print("subject:",subject)
	item=sheduler.chooseItem(request.user,subject)
	print item
	return render(request,'pop/pop.html',{'item':item})
		
def process(request):
	if request.method=='POST':
		postData=request.POST
		print("postData:",postData)
		user=request.user
		item_pk=int(postData['item_pk'])
		score=int(postData['score'])
		item=Item.objects.get(pk=item_pk)
		print("Post item:",item)
		master=Master.objects.filter(user=request.user).filter(item=item)[0]
		master.score+=score
		print("master:",master)
		print("score:",master.score)
		master.save()
		response={'status':1}
		return HttpResponse(json.dumps(response),content_type='application/json')
	else:
		return HttpResponse('invalid request')
