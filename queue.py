class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def maxSize(self):
        return 64

    def isFullSize(self):
        return self.size() == self.maxSize()

    def getItems(self):
        return self.items