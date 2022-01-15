def readfile(file):
    filehandle = open (file, 'r', encoding="utf8")
    thewholefile = filehandle.read()
    filehandle.close()
    return thewholefile

def readline(file):
    filehandle = open (file, 'r', encoding="utf8")
    thewholefile = filehandle.readlines()
    filehandle.close()
    return thewholefile

def savenew(file,data):
    filehandle = open (file, 'x')
    filehandle.write(data)
    filehandle.close()

#append data in end file
def saveappend(file,data):
    filehandle = open (file, 'a+')
    filehandle.write(data)
    filehandle.close()
