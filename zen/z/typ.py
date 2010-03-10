class String(str):
    __init__(self,*args,*keywords):
        str.__init__(self)
    
class List(list):
    __init__(self,arg):
        self.extend(_iterable(arg))
        list.__init__(self)        

class Float(float):
    __init__(self,*args,*keywords):
        float.__init__(self)        
        
class Int(int):
    __init__(self,*args,*keywords):
        int.__init__(self)
        
def _iterable(arg):
    if type(arg).__name__=='NoneType':
        return []
    if not _isIterable(arg):
        if isinstance(arg,(basestring,float,int,long)):
            return [arg]
        else:
            return []
    else:
        return arg

def _isIterable(arg):
    return hasattr(arg,'__iter__') and not isinstance(arg,basestring)