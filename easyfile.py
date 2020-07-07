def readfile(file):
    filehandle = open (file, 'r')
    thewholefile = filehandle.read()
    filehandle.close ()
    return thewholefile

def savefile(file,data):
    filehandle = open (file, 'a')
    filehandle.write(data)
    filehandle.close ()
