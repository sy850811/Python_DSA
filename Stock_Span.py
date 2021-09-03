
from sys import stdin

def stockSpan(arr, n) :
    stack = []
    freq = []
    for i in range(len(price)):
        while (len(stack)!=0 and arr[stack[-1]] < arr[i]):
            stack.pop()
        if len(stack)==0:
            freq.append(i+1)
        else:
            freq.append(i - stack[-1])
        stack.append(i)
    return freq


































'''-------------- Utility Functions --------------'''




def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
