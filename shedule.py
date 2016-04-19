import random
from pop.models import Master


def choose_level(user,catagory):
	degree=Master.objects.filter(user=user)[0].degree[catagory]
	if len(degree['hover'])<6:
		choice='new'
	else:
		rlist=['new']*2
		rlist.extend(['hover']*7)
		rlist.extend(['familiar'])
		choice=random.choice(rlist)
		if not degree[choice]:
			choose_level(user,catagory)
	return choice

def choose_item(user,catagory,choice):
	if 
	



