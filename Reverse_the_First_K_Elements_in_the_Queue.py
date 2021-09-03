
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def reverseQueue(inputQueue) :
    if inputQueue.empty():
        return
    data = inputQueue.get()
    reverseQueue(inputQueue)
    inputQueue.put(data)

def reverseKElements(inputQueue, k) :
    outputQueue = queue.Queue()
    for i in range(k):
        outputQueue.put(inputQueue.get())
    reverseQueue(outputQueue)
    
    for i in range(inputQueue.qsize()):
        outputQueue.put(inputQueue.get())
    return outputQueue































    



'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")
