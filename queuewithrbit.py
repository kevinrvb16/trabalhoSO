class QueueWithRBit:

    def __init__(self):
        self.items = []
        self.isReferencedList = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.isReferencedList.insert(0, True)
        self.items.insert(0, item)
        return self.items[0]

    def dequeue(self):
        self.isReferencedList.pop()
        return self.items.pop()

    def size(self):
        return len(self.items)

    def maxSize(self):
        return 64

    def isFullSize(self):
        return self.size() == self.maxSize()

    def getItems(self):
        return self.items

    def getIsReferencedList(self):
        return self.isReferencedList

    def getFirstItem(self):
        return self.items[self.size()-1]

    def getFirstIsReferenced(self):
        return self.isReferencedList[self.size()-1]

    def setFirstIsReferenced(self, isReferenced ):
        self.isReferencedList[self.size()-1] = isReferenced

    def setIsReferenced(self, item, isReferenced):
        indexOfItem = self.getIndexOfItem(item)
        self.isReferencedList[indexOfItem] = isReferenced

    def sendToEndOfQueue(self):
        lastItem = self.getFirstItem()
        self.setFirstIsReferenced(False)
        lastIsReferenced = self.getFirstIsReferenced()
        self.dequeue()
        self.items.insert(0, lastItem)
        self.isReferencedList.insert(0, lastIsReferenced)

    def getIndexOfItem(self, item):
         return self.items.index(item)

    def giveSecondChance(self, referencedPage):
        while(True):
            if self.getFirstIsReferenced() == True:
                self.sendToEndOfQueue()
            else:
                self.dequeue()
                self.enqueue(referencedPage)
                return False
