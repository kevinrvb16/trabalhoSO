class Node:
    def __init__(self, page = 0, next_node = None):
        self.page = page
        self.next_node = next_node

    def __repr__(self):
        return '%s -> %s' % (self.page, self.next_node)