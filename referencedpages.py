import random

def  referencedPages():

    firstPage = 0
    lastPage = 255
    referencedPages =[]
    writeReferenceFile = open("./referencedpages.txt", "w")

    for n in range(10000):
        referencedPage = (random.randrange(firstPage, lastPage))
        referencedPages.append(referencedPage)

    writeReferenceFile.write(str(referencedPages).strip('[]'))
    writeReferenceFile.close()
    readReferenceFile = open("./referencedpages.txt", "r")

    for line in readReferenceFile:
        readingReferencedPages = line.rstrip(' ')
    readReferenceFile.close()
    return readingReferencedPages
referencedPages()