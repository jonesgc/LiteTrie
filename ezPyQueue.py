# A queue implementation in pyhton using simple language and terms.

class ezQueue:
    top = None
    bot = None
    container = []

    def __init__(self):
        pass

    def getTop(self):
        return top
    
    def getBot(self):
        return bot
    
    def popTop(self):

        popped = self.container[0]
        self.container.pop(0)
            
        return popped

    def place(self,item):
        self.container.insert(0, item)

        l = len(self.container)

        if l == 1:
            self.top = item
            self.bot = item
        elif l > 1:
            self.bot = item
        
        return True
    
    def printEzQueue(self):

        x = 0

        for i in self.container:
            print("Item at: {}, is: {}" .format(x, i))
            x= x + 1

        return True
    
    def isEmpty(self):
        if not self.container:
            return True
        else:
            return False