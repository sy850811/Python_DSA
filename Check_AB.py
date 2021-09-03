## Read input as specified in the question.
## Print output as specified in the question.
def checkab(str,state):
    
    if state == 0:
        if str[0] == 'a':
            return checkab(str[1:],0)
        
        elif str[0] == '\n':
            return True
        
        elif str[0] == 'b':
            return checkab(str[1:],1)   
        
    if state == 1:
        if str[0] == 'b':
            return checkab(str[1:],2)
        
    if state == 2:
        
        if str[0] == 'a':
            return checkab(str[1:],0)
        
        elif str[0] == '\n':
            return True
        
    if state == 5:
        if str[0] == 'a':
            return checkab(str[1:],0)
        
    return False

str = input() + '\n'
if checkab(str,5):
    print("true")
else:
    print("false")


            
