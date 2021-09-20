from fila import Fila

def Fifo(referencedPages):

    q = Fila()
    countPageFaults = 0

    for referencedPage in referencedPages:
        if referencedPage not in q.getItems():
            if (q.isEmpty() or not q.isFullSize()):
                    q.enqueue(referencedPage)
                    countPageFaults += 1
            else:
                q.dequeue()
                q.enqueue(referencedPage)
                countPageFaults += 1
    print("Páginas na memória: " + str(q.getItems()))
    print("Quantidade de PageFaults: " + str(countPageFaults))
