from frame import Frame
from page import Page
import random
import time
from collections import defaultdict


def NRU(referencedPages):

    initialTime = time.time()
    dict = defaultdict(lambda: defaultdict(dict))
    ##dict = { 3: {1,0}, 4: [1,0], 5: 30,}##
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
                print("Página adicionada: "+ str(referencedPage))
            elif(len(dict) == maxLen):
                print("PageFault!")
                for allocatedPage in dict.keys():
                    if (dict[allocatedPage].get('referenced') == 0 and dict[allocatedPage].get('modified') == 0):
                        classes[0].append(int(allocatedPage))
                    elif (dict[allocatedPage].get('referenced') == 0 and dict[allocatedPage].get('modified') == 1):
                        classes[1].append(int(allocatedPage))
                    elif (dict[allocatedPage].get('referenced') == 1 and dict[allocatedPage].get('modified') == 0):
                        classes[2].append(int(allocatedPage))
                    elif (dict[allocatedPage].get('referenced') == 1 and dict[allocatedPage].get('modified') == 1):
                        classes[3].append(int(allocatedPage))
                if(len(classes[0]) != 0):
                    print("entrou if0")
                    randomPageToDelete = (random.choice(classes[0]))
                if(len(classes[1]) != 0):
                    print("entrou if1")
                    randomPageToDelete = (random.choice(classes[1]))
                if(len(classes[2]) != 0):
                    print("entrou if2")
                    randomPageToDelete = (random.choice(classes[2]))
                if(len(classes[3]) != 0):
                    print("entrou if3")
                    print(classes[3])
                    randomPageToDelete = (random.choice(classes[3]))
                print(dict)
                dict.pop(str(randomPageToDelete))
                print("Página que será excluída" + str(randomPageToDelete))
                dict[referencedPage] = {'modified': 1, 'referenced': 1}
                countPageFaults += 1
        else:
            dict[referencedPage]['referenced'] = 1
            print("Página já está no quadro: " + str(referencedPage))
        classes[0].clear()
        classes[1].clear()
        classes[2].clear()
        classes[3].clear()

        changeReferencedToZero += 1
        if(changeReferencedToZero%13 == 0):
            for page in dict:
                dict[page].update(referenced = 0)
            
    print("quantidade de PageFaults: " + str(countPageFaults))
    print(dict)

    finalTime = time.time()
    print("Tempo para executar nru em milissegundos" + (str(finalTime - initialTime)))