from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise(root):
    q = queue.Queue()
    if root == None:
        return
    q.put(root)
    # print(root.data)
    
    while not q.empty():
        current = q.get()
        print(current.data,end = '')
        print(':L:',end='')
        if current.left != None:
            q.put(current.left)
            print(current.left.data,end = '')
        else:
            print('-1',end = '')
        print(',R:',end='')
        if current.right != None:
            print(current.right.data)
            q.put(current.right)
        else:
            print('-1')
    return































    



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
