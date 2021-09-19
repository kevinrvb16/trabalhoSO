from linkedlist import LinkedList

def LRU(referencedPages):
    linkedlist = LinkedList()
    for referencedPage in referencedPages:
        linkedlist.insertAtStart(referencedPage)
    print('Páginas na memória: %s' % linkedlist)
    print("Quantidade de PageFaults: " + str(linkedlist.pageFault))