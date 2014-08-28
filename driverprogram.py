import theinnerworkings

def main():
    
    
    alst = theinnerworkings.lst()
    """
    alst.addstuff(5)
    alst.addstuff(3)
    alst.addstuff(1)
    alst.addstuff(6)
    alst.addstuff(9)
    """
    
    phylagrabber = open('phyla.txt', 'r')
    for line in phylagrabber:
            
            
            x = line
            
            x.split()
            
            number = x.find(":")
            alst.addstuff(x[0:number])
            
    
    
    print "Is Rotifera in the list?"
    print "\n"
    x = alst.pulloneout("Rotifera")
    
    print x
    print "\n"
    print "Is Zonicefria in the list?"
    print "\n"
    x = alst.pulloneout("Zonicefria")
    
    print x
    print "\n"
    print "Here is the full list"
    print "\n"
    alst.returnall()
    
    
if __name__ == '__main__':
    main()

    
        
    