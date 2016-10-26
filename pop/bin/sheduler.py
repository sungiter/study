import random
import json
import logging

from django.core import serializers

from pop.models import Statistics,Master

logger=logging.getLogger(__name__)

def preProcess(statistic):
	try:
		logger.debug("deserialize data")
		newList=[]
		studyingList=[]
		rememberedList=[]
		for obj in serializers.deserialize('json',statistic.new):
			newList.append(obj.object)
		for obj in serializers.deserialize('json',statistic.studying):
			studyingList.append(obj.object)
		for obj in serializers.deserialize('json',statistic.remembered):
			rememberedList.append(obj.object)
	except serializers.json.DeserializationError,e:
		#logger.debug("statistic is empty")
		newList=statistic.new=[]
		studyingList=statistic.studying=[]
		rememberedList=statistic.remembered=[]
	if len(newList)<10:
		try:
			master=Master.objects.filter(score=0).order_by('-id')[0]
			logger.debug("master:%s"%master)
			if master not in newList:
				newList.append(master)
		except IndexError,e:
			print "Error"
			pass			
	if len(studyingList)<5:
		try:
			master=newList[0]
			if master not in studyingList:
				studyingList.append(master)
				newList.pop(0)
		except IndexError,e:
			pass
	print studyingList
	statistic.new=serializers.serialize('json',newList)
	statistic.studying=serializers.serialize('json',studyingList)
	statistic.remembered=serializers.serialize('json',rememberedList)
	statistic.save()
	statistic={'new':newList,'studying':studyingList,'remembered':rememberedList}
	return statistic
	
def chooseLevel():
	randNum=random.random()
	if randNum<=0.1:
		return 'new'
	elif randNum>=0.9:
		return 'remembered'
	else:
		return 'studying'


def chooseItem(statistic):
	statistic=preProcess(statistic)
	logger.info("statistic:",statistic)
	masterList=[]
	while not masterList:
		level=chooseLevel()
		print("level:",level)
		masterList=statistic[level]
	master=random.choice(masterList)
	item=master.item.get()
	return item

