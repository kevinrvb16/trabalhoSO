from linkedlist import LinkedList

def LRU(referencedPages):
    linkedlist = LinkedList()
    for referencedPage in referencedPages:
        print('Lista: %s' % linkedlist)
        linkedlist.insertAtStart(referencedPage)
    print('Lista: %s' % linkedlist)
    print("Quantidade de PageFaults: " + str(linkedlist.pageFault))