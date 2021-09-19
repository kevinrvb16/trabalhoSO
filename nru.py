import random
from collections import defaultdict

def NRU(referencedPages):

    dict = defaultdict(lambda: defaultdict(dict))
    maxLen = 64
    countPageFaults = 0
    classes = [[], [], [], []]
    randomPageToDelete = -1
    modifiedRange = [0,1]
    changeReferencedToZero = 0

    for referencedPage in referencedPages:
        if referencedPage not in dict:
            if (len(dict)==0 or len(dict) < maxLen):
                dict[referencedPage] = {'referenced': 1, 'modified': random.choice(modifiedRange)}
                countPageFaults += 1
            elif(len(dict) == maxLen):
                for allocatedPage in dict.keys():
                    if (dict[allocatedPage].get('referenced') == 0 and dict[allocatedPage].get('modified') == 0):
                        classes[0].append(int(allocatedPage))
                    elif (dict[allocatedPage].get('referenced') == 0 and dict[allocatedPage].get('modified') == 1):
                        classes[1].append(int(allocatedPage))
                    elif (dict[allocatedPage].get('referenced') == 1 and dict[allocatedPage].get('modified') == 0):
                        classes[2].append(int(allocatedPage))
                    elif (dict[allocatedPage].get('referenced') == 1 and dict[allocatedPage].get('modified') == 1):
                        classes[3].append(int(allocatedPage))
                if(len(classes[0]) > 0):
                    randomPageToDelete = (random.choice(classes[0]))
                elif(len(classes[1]) != 0):
                    randomPageToDelete = (random.choice(classes[1]))
                elif(len(classes[2]) != 0):
                    randomPageToDelete = (random.choice(classes[2]))
                elif(len(classes[3]) != 0):
                    print(classes[3])
                    randomPageToDelete = (random.choice(classes[3]))
                ##print(dict)  ##descomentar apenas para teste
                dict.pop(str(randomPageToDelete))
                dict[referencedPage] = {'referenced': 1, 'modified': random.choice(modifiedRange)}
                countPageFaults += 1
                classes[0].clear()
                classes[1].clear()
                classes[2].clear()
                classes[3].clear()
        else:
            dict[referencedPage]['referenced'] = 1        
        changeReferencedToZero += 1
        if(changeReferencedToZero == 3 ):
            for page in dict:
                dict[page].update(referenced = 0)
            changeReferencedToZero = 0
    print("Páginas na memória" + str(dict))
    print("quantidade de PageFaults: " + str(countPageFaults))
