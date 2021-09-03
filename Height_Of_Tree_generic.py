import sys
import queue

#main

sys.setrecursionlimit(10**6)

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []


## Read input as specified in the question.

def takeInput():
    que = queue.Queue()
    i = 0
    inp = [int(i) for i in input().split()]
    if inp[i] == -1:
        return None
    root = BinaryTreeNode(inp[i])
    que.put(root)
    
    while not que.empty():
        node = que.get()
        # print(inp[i])
        i+=1
        
        size = inp[i]
        for j in range(size):
            # print(inp[i])
            i+=1
            childNode = BinaryTreeNode(inp[i])
            que.put(childNode)
            node.children.append(childNode)
    return root
    



## Print output as specified in the question.
def printGenricTree(root):
    if root == None:
        return
    print(root.data,end = ' : ')
    for i in root.children:
        print( i.data,end = ',')
    print()
    for i in root.children:
        printGenricTree(i)
        



def maxHeight(root):
    if root == None:
        return 0
    height = 0
    for i in root.children:
        h =  maxHeight(i)
        height = h if h > height else height
    return height + 1


## Read input as specified in the question.

# def takeInput(current = 0):
#     if inputList[current] == -1:
#         return current,None
#     data = inputList[current]
#     current+=1
#     size = inputList[current]
#     root = BinaryTreeNode(data)
#     for i in range(size):
#         current +=1
#         current , child = takeInput(current)
#         # print(data ,'(',size,')', '-->',child.data)
#         root.children.append(child)
#     return current,root




root = takeInput()
# printGenricTree(root)
print(maxHeight(root))
        
