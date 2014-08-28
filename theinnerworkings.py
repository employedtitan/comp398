class node:
    
    def __init__(self, word):
        self.word = word
        self.upnext = None 
        
    
    def here(self):
        return self.word
    
    def nextnode(self):
        return self.upnext
    
    def newword(self, werd):
        self.word = werd
        
    def newupnext(self, nxt):
        self.upnext = nxt
        
        

class lst:
    
    def __init__(self):
        self.head = None
        
    def addstuff(self, stuff):
        temp = node(stuff)
        temp.newupnext(self.head)
        self.head = temp
    
    def pulloneout(self, searchable):
        begin = self.head
        
        gotit = "It is not in the list"
        
        i = False
        while begin != None and not i:
            if begin.here() == searchable:
                gotit = "It is in the list"
                i = True
            else:
                begin = begin.nextnode()
                
        return gotit
        
    def returnall(self):
        begin = self.head
        
        while begin != None:
            print begin.here()
            begin = begin.nextnode()
        
        
def main():
    """
    nothing to see here
    """
    
    pass


if __name__ == '__main__':
    main()