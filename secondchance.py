from queuewithrbit import QueueWithRBit

def SecondChance(referencedPages):

    q = QueueWithRBit()
    countPageFaults = 0

    for referencedPage in referencedPages:
        if referencedPage not in q.getItems():
            if (q.isEmpty() or not q.isFullSize()):
                q.enqueue(referencedPage)
                countPageFaults += 1
            else:
                q.giveSecondChance(referencedPage)
                countPageFaults += 1
        else:
            q.setIsReferenced(referencedPage, True)   
    print("Páginas na memória" + str(q.getItems()))
    print("Quantidade de PageFaults: " + str(countPageFaults))
