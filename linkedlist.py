from node import Node

class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.pageFault = 0

    def __repr__(self):
        return str(self.head)

    def insertAtStart(self, new_node):
        if self.len() < self.maxLen():
            if (self.search(new_node)):
                pointer = self.search(new_node)
                pointerNext = pointer.next_node
                pointer.next_node = self.head
                self.head = pointer
                while(pointer.next_node != self.head):
                    pointer = pointer.next_node
                pointer.next_node = pointerNext
            else:
                new_node = Node(new_node)
                new_node.next_node = self.head
                if(self.head == None ):
                    self.tail = new_node
                elif(self.head.next_node == new_node):
                    self.tail = new_node.next_node
                self.head = new_node
                self.pageFault += 1
        else:
            if (self.search(new_node)):
                pointer = self.search(new_node)
                pointerNext = pointer.next_node
                pointer.next_node = self.head
                self.head = pointer
                while(pointer.next_node != self.head):
                    pointer = pointer.next_node
                pointer.next_node = pointerNext
                while (pointer.next_node):
                    pointer = pointer.next_node
                self.tail = pointer
            else:
                new_node = Node(new_node)
                new_node.next_node = self.head
                if(self.head == None ):
                    self.tail = new_node
                elif(self.head.next_node == new_node):
                    self.tail = new_node.next_node
                self.head = new_node
                self.removeLast()
                self.pageFault += 1


    def search(self, value):
        pointer = self.head
        while pointer and pointer.page != value:
            pointer = pointer.next_node
        return pointer

    def removeLast(self):
        assert self.head, "Não é possível remover pois a lista é vazia."
        pointer = self.head
        while pointer and pointer.next_node != self.tail:
            pointer = pointer.next_node
        removed = self.tail
        pointer.next_node = None
        self.tail = pointer
        return removed.page

    def len(self):
        size = 0
        pointer = self.head
        while pointer != None:
            pointer = pointer.next_node
            size += 1
        return size

    def maxLen(self):
        return 64