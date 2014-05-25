import os, sys


def getFullFilename(prefix, filename, ext):
    return os.path.join(os.path.dirname(filename),str(prefix)+os.path.splitext(os.path.basename(filename))[0]+"."+str(ext))


def cleanFilenames(filenames):
    filenames = [ i for i in filenames if not os.path.splitext(i)[1] == '.dat' and os.path.isfile(i) ]
    filenames = [ i for i in filenames if not os.path.splitext(i)[1] == '.txt' ]
    return filenames
