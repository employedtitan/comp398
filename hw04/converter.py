import string
class converter:
    
    def __init__(self):
        
        self.filestorage = ""
        self.empty = ""
    
    def ptag():
        
        pass
    def atag():
        pass
    
    def honetag():
        pass
    
    def htwotag():
        pass
    
    def hthreetag():
        pass
    
    
    def btag(self):
        end = ""
        inbq = False
        
        for line in self.filestorage:
            if line[0] == ">":
                empty = "<blockquote>" + empty
                inbq = True
                
            elif line[0] == ">" and inbq == True:
                pass
            
            elif line[0] != ">":
                empty = empty + line
                
            elif line[0] == "\n":
                empty = empty + "</blockquote>"
                inbq = False
                

    def readin(self, filename):
        self.throwaway = open(filename, 'r')
        
    def closefile(self):
        self.throwaway.close()
        
    def doitall(self):
        self.filestorage = self.btag()
        
        #self.filestorage = ptag()
        #self.filestorage = honetag()
        #self.filestorage = htwotag()
        #self.filestorage = hthreetag()
        #self.filestorage = atag()
        
        return self.filestorage
        
def main():
    
    a = converter()
    
    newtext = ""
    a.readin('test.md.txt')
    newtext = a.doitall()
    a.closefile()
    
    q = open('output.html', 'w')
    q.write(str(newtext))
    q.close()
   
   
if __name__ == '__main__':
    main()
 

        
        