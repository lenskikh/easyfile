def readfile(filename,**kwargs):
    
    try:
        characterSet = kwargs["characterSet"]
    except:
        characterSet = 'utf-8'

    with open(filename, 'r', encoding = characterSet) as filehandle:
        thewholefile = filehandle.read()
    return thewholefile

def readline(filename,**kwargs):

    try:
        characterSet = kwargs["characterSet"]
    except:
        characterSet = 'utf-8'    

    with open(filename, 'r', encoding = characterSet) as filehandle:
        thewholefile = filehandle.readlines()
    return thewholefile

def savenew(filename,data,**kwargs):

    try:
        characterSet = kwargs["characterSet"]
    except:
        characterSet = 'utf-8'    

    with open(filename, 'w',encoding = characterSet) as filehandle:
        filehandle.write(data)  

#append data in end file
def saveappend(filename,data,**kwargs):

    try:
        characterSet = kwargs["characterSet"]
    except:
        characterSet = 'utf-8'    

    with open(filename, 'a+',encoding = characterSet) as filehandle:
        filehandle.write(data)

