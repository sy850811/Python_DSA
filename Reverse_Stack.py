from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
def reversePop(s1, s2):
        if len(s2) == 0:
            return
        data = s2.pop()
        reversePop(s1,s2)
        s1.push(s2.pop)

def reverseStack(inputStack, extraStack) :
    while not isEmpty(inputStack):
        extraStack.append(inputStack.pop())
    # print("----",not isEmpty(inputStack),not isEmpty(extraStack))
    while not isEmpty(inputStack) :
        print(inputStack.pop(), end = " ")
        
    while not isEmpty(extraStack) :
        print(extraStack.pop(), end = " ")
    
    
        
    reversePop(inputStack,extraStack)
            































'''-------------- Utility Functions --------------'''

#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Taking input using fast I/o method
def takeInput() :
	size = int(stdin.readline().strip())
	inputStack = list()

	if size == 0 :
		return inputStack


	values = list(map(int, stdin.readline().strip().split(" ")))
	inputStack = values

	return inputStack


# Main
inputStack = takeInput()
emptyStack = list()

reverseStack(inputStack, emptyStack)

while not isEmpty(inputStack) :
	print(inputStack.pop(), end = " ")
