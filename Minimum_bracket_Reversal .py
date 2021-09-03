
from sys import stdin

def countBracketReversals(inputString) :
    rev = 0
    stack = []
    for i in inputString:
        if i is '{':
            stack.append(i)
        else:
            if len(stack) == 0:
                rev+=1
                stack.append('{')
            else:
                stack.pop()
    if len(stack)%2 == 0:
        rev+= len(stack)/2
        return int(rev)
    else:
        return -1
        






























#main
print(countBracketReversals(stdin.readline().strip()))
