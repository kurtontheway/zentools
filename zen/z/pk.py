"Package utilities."
import sys,os
from modulefinder import AddPackagePath,ModuleFinder
from zen.iterable import iterable
def moveDef(a,b,**keywords):
    """moveDef(source,destination,**keywords)
Moves the contents of one module to another, 
or a function or class from one module into a another, 
and fix references to aforementioned module or class within specified packages.
Arguments
    source: string denoting an existing function, class, or module ( including namespace ).
    destination: string denoting a new or existing function, class, module, or file path. 
Options
    searchAll: bool
        if True: check all installed packages to see if they reference the module being moved / renamed       
    packages OR pk: list of strings
        a list of packages or modules to check in addition to the parent package
    """
    #parse options & arguments
    packages=[]
    searchAll=False
    backup=False
    shortNames={
        'sa':'searchAll',
        'pk':'packages',
        'bk':'backup'
    }
    for k in keywords:
        if k in locals():
            exec(k+'=keywords[k]')
        elif k in shortNames:
            exec(shortNames[k]+'=keywords[k]')
    #see if b is a module or a path
    #
    inputType=["module","module"]
    try:
        ib=__import__(b)
        if "__path__" in dir(ib):#it's a package
            inputType[1]="package"
    except:
        if os.path.isdir(b):
            AddPackagePath(os.path.basename(b),b)
            b=os.path.basename(b)
            inputType[1]="package"
        elif os.path.isfile(b):
            sys.path.append(os.path.dirname(b))
            b='.'.join(os.path.basename(b).split('.')[:-1])
        ib=__import__(b)
    try:#if it's a module move the entire contents
        ia=__import__(a)
        get="*"
        if "__path__" in dir(ia):#it's a package
            inputType[0]="package"
    except:#otherwise find what it needs
        get=a.split('.')[-1]
        ia=__import__(a.split('.')[:-1])
        if "__path__" in dir(ia):#it's a package
            inputType[0]="package"
    #mf=ModuleFinder(path=None)