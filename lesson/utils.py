from .models.human_model import Human
import random

def generate_humanID():
	gethumanID 	= ''.join(random.choice('0123456789') for i in range(10))
	getAlpha 	= ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(2))
	humanID   	= getAlpha+gethumanID
	
	while Human.objects.filter(humanID=humanID).exists():
		gethumanID 	= ''.join(random.choice('0123456789') for i in range(10))
		getAlpha 	= ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(2))
		humanID   	= getAlpha+gethumanID
		
	return humanID