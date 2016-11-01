import os
import sys
import random
import string
import django


sys.path.append('/home/tmyyss/project/study')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "study.settings")
django.setup()
from django.contrib.auth.models import User

from pop.models import Subject,Category,Item,Master

#Add subject
#s1=Subject()
#s1.subject='s1'
#s2=Subject()
#s2.subject='s2'
#s3=Subject()
#s3.subject='s3'
#s1.save()
#s2.save()
#s3.save()

#Add category
#for i in range(1,11):
#	c=Category()
#	c.subject=random.choice([s1,s2,s3])
#	c.category='c%d'%i
#	c.save()

#Add item
#letters=string.ascii_letters+string.digits
#categoryList=Category.objects.all()
#for i in range(1,100001):
#	item=Item()
#	item.category=random.choice(categoryList)
#	item.question=''.join(random.sample(letters,10))
#	item.answer=''.join(random.sample(letters,20))
#	item.save()


#Add user
user1=User.objects.create_user('user1','tmyyss@126.com','user1password')
user2=User.objects.create_user('user2','tmyyss@163.com','user2password')
user3=User.objects.create_user('user3','tmyyss@gmail.com','user3password')
user1.save()
user2.save()
user3.save()

#Add master
for user in (user1,user2,user3):
	itemList=Item.objects.all()
	for item in itemList:
		master=Master()
		master.user=user
		master.item=item
		master.save()



