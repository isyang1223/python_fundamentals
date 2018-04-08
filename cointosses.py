import random

def cointosses():
    counthead = 0
    counttail = 0
    print "Starting the program..."
    for i in range(0, 5000):
        coin = random.randint(0, 1)
        if coin == 1:
            coin = "head"
            counthead +=1
        else:
            coin = "tail"
            counttail +=1
        print "Attempt #"+str(i)+": Throwing a coin... It's a "+ coin +"! ... Got "+ str(counthead) +" head(s) so far and " + str(counttail) + " tail(s) so far"
    print "Ending the program, thank you!"    
    
    

cointosses()