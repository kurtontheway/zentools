from zen.isIterable import isIterable

def iterable(arg):
	if type(arg).__name__=='NoneType':
		return []
	if not isIterable(arg):
		if isinstance(arg,(basestring,float,int,long)):
			return [arg]
		else:
			return []
	else:
		return arg
