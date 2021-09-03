from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

import math
#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    if root == None:
        return
    arr = queue.Queue()
    arr.put(root)
    arr.put(None)
    count = 2
    flag = False
    while not arr.empty():
        current = arr.get()
        if current == None:
            if flag:
                return
            print()
            arr.put(None)
            flag = True
            continue
        if current != -1:
            print(current.data,end = ' ')
            if current.left != None:
                arr.put(current.left)
            if current.right != None:
                arr.put(current.right)
        flag = False
            
            



































                

#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


# Main
root = takeInput()
printLevelWise(root)
