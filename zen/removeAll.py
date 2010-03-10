from zen.isIterable import isIterable

def removeAll(removeList, origList):
	
	if not isIterable(origList):
		if isinstance(origList,(basestring,float,int,long)):
			origList=[origList]
		else:
			return []
	if not isIterable(removeList):
		if isinstance(removeList,(basestring,float,int,long)):
			removeList=[removeList]
		else:
			return []
	returnVal=[]
	if isIterable(removeList):
		for o in origList:
			if o not in removeList:
				returnVal.append(o)
	return returnVal
