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
	return choice,degree[choice],degree

def choose_item(degrees):
	return random.choice(degrees.keys)



def make_desicion(item,answer):
	if answer='y':
		if degrees[item]<100
			degress[item]+=10
			if degress=100:
				del degree['hover'][item]
				degree['familiar'][item]=100
	else:
		if degress[item]>0:
			degress[item]-=10
		else:
			degress[item]=0
	



