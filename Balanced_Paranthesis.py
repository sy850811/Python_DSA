
from sys import stdin


def isBalanced(expression) :
    stack = []
    for i in expression:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif i == '}':
            if len(stack) == 0:
                return False
            if stack[-1] == '{}':
                stack.pop()
            else:
                return False
        elif i == ']':
            if len(stack) == 0:
                return False
            if stack[-1] == '[':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
            
        
        

























	




#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
