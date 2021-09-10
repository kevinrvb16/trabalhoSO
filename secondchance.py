from queuewithrbit import QueueWithRBit

def SecondChance(referencedPages):

    q = QueueWithRBit()
    countPageFaults = 0

    for referencedPage in referencedPages:
        if referencedPage not in q.getItems():
            if (q.isEmpty() or not q.isFullSize()):
                q.enqueue(referencedPage)
                print("Página adicionada: "+ str(referencedPage))
                countPageFaults += 1
            elif(q.isFullSize()):
                print("PageFault!")
                q.giveSecondChance(referencedPage)
                countPageFaults += 1
        else:
            q.setIsReferenced(referencedPage, True)
            print("Página já está na fila: " + str(referencedPage))
            
    print("Quantidade de PageFaults: " + str(countPageFaults))
    print(q.getItems())
