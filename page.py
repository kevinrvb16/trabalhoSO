class Page:
    
    def __init__(self, n):
        self.page = n
        self.isReferenced = True

    def getPage(self):
        return self.page

    def setPage(self, page):
        self.page = page

    def setIsReferenced(self, isReferenced):
        self.isReferenced = isReferenced

    def getIsReferenced(self):
        return self.isReferenced