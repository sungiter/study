import random
import json
import logging

from django.core import serializers

from pop.models import Statistics,Master

logger=logging.getLogger(__name__)

def preProcess(user,subject):
	newList=[]
	studyingList=[]
	rememberedList=[]
	try:
		statisticsObj=Statistics.objects.filter(user=user)[0]
		print("statisticsObj:",statisticsObj)
		statisticsDict=json.loads(statisticsObj.statistics)
		dataOfSubject=statisticsDict.setdefault(subject,{})
		print("deserialize data")
		print("dataOfSubject:",dataOfSubject)
		if dataOfSubject:
			for obj in serializers.deserialize('json',dataOfSubject['new']):
				master=Master.objects.get(pk=obj.object.pk)
				if master.score>0:
					studyingList.append(master)
				else:
					newList.append(master)
			for obj in serializers.deserialize('json',dataOfSubject['studying']):
				master=Master.objects.get(pk=obj.object.pk)
				if master.score>=10:
					rememberedList.append(master)
				else:
					studyingList.append(master)
			for obj in serializers.deserialize('json',dataOfSubject['remembered']):
				master=Master.objects.get(pk=obj.object.pk)
				if master.score<10:
					studyingList.append(master)
				else:
					rememberedList.append(master)
		else:
			print("Initial the statistic")
	                #statisticsDict=statisticsObj.statistics={}
        	        #dataOfSubject=statisticsDict.setdefault(subject,{})
	except IndexError,e:
		print("Initial the statistic")
		statisticsObj=Statistics()
		statisticsObj.user=user
		statisticsDict=statisticsObj.statistics={}
		dataOfSubject=statisticsDict.setdefault(subject,{})
	print("get statisticsObj:",statisticsObj)
	if not newList:
		try:
			master=Master.objects.filter(user=user).filter(item__category__subject__subject=subject).filter(score=0).order_by('-id')[:10]
			print "add master to newList:",master
			newList.extend(master)
		except IndexError,e:
			pass			
	if len(studyingList)<10:
		try:
			master=newList[-1]
			print "add master to studyingList:",master
			if master not in studyingList:
				studyingList.append(master)
				newList.remove(master)
				print "after pop:",newList
			else:
				newList.remove(master)
		except IndexError,e:
			pass
	dataOfSubject['new']=serializers.serialize('json',newList)
	dataOfSubject['studying']=serializers.serialize('json',studyingList)
	dataOfSubject['remembered']=serializers.serialize('json',rememberedList)
	print("save statisticsObj:",statisticsObj)
	statisticsObj.statistics={subject:dataOfSubject}
	print("dataOfSubject:",dataOfSubject)
	statisticsStr=json.dumps(statisticsObj.statistics)
	statisticsObj.statistics=statisticsStr
	statisticsObj.save()
	return {'new':newList,'studying':studyingList,'remembered':rememberedList}
	
def chooseLevel():
	randNum=random.random()
	if randNum<=0.2:
		return 'new'
	elif randNum>=0.8:
		return 'remembered'
	else:
		return 'studying'


def chooseItem(user,subject):
	statistic=preProcess(user,subject)
	logger.info("statistic:",statistic)
	print statistic
	if not any(statistic.values()):
		print("All is empty")
		item=None
	elif not statistic['new'] and not statistic['studying'] and statistic['remembered']:
		print("all is remembered")
		item={"status":1}
	else:
		masterList=[]
		while not masterList:
			level=chooseLevel()
			print "choose level:",level
			masterList=statistic[level]
		master=random.choice(masterList)
		print("choose master:",master)
		item=master.item
		print("choose item:",item)
	return item


