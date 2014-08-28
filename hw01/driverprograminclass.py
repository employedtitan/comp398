import theinnerworkings

def main():
    
    
    alst = theinnerworkings.lst()
    blst = theinnerworkings.lst()
    """
    alst.addstuff(5)
    alst.addstuff(3)
    alst.addstuff(1)
    alst.addstuff(6)
    alst.addstuff(9)
    """
    
    phylagrabber = open('class assignment.txt', 'r')
    for line in phylagrabber:
            
            
            x = line
            
            
            
            
            alst.addstuff(x)
            
    
    
    
    
    abbregrabber = open('abbreclass.txt', 'r')
    
    for line in abbregrabber:
        
        n = line
        
        blst.addstuff(n)
        
        

    print "\n"
    print "Here is the full list"
    print "\n"
    alst.returnall()
    
    blst.returnall()
    
if __name__ == '__main__':
    main()

    
        
    