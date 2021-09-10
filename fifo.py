from queue import Queue

def Fifo(referencedPages):

    q = Queue()
    countPageFaults = 0

    for referencedPage in referencedPages:
        if referencedPage not in q.getItems():
            if (q.isEmpty() or not q.isFullSize()):
                    q.enqueue(referencedPage)
                    print("Página adicionada: " + str(referencedPage))
                    countPageFaults += 1
            elif(q.isFullSize()):
                print("PageFault! Removendo  último da fila: " + str(q.dequeue()))
                q.enqueue(referencedPage)
                print("Alocado primeiro da fila: " + str(referencedPage))
                countPageFaults += 1
        else:
            print("Página já está na fila: " + str(referencedPage))
            
    print("Quantidade de PageFaults: " + str(countPageFaults))
    print(q.getItems())
