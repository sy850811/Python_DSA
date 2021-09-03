from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def nodesAtDistanceK(node, data, k, ptr=None,isDown=False) :
    if node == None:
        # print ('a','k=',k)
        if ptr != None:
            k = k + 1
        return ptr,k,isDown
    if node.data == data:
        isDown = True
        # print (node.data,'b','k=',k)
        if ptr!=None:
            # print (node.data,'c','k=',k)
            return node,k-1,isDown
        else:
            # print (node.data,'d','k=',k)
            ptr = node
    if ptr!= None:
        # print (node.data,'e','k=',k)
        if k == 0:
            # print('f','k=',k)
            print(node.data)
            return ptr,k-1,isDown
        else:
            # print (node.data,'n','k=',k)
            nodesAtDistanceK(node.left,data,k-1,ptr,isDown)
            nodesAtDistanceK(node.right,data,k-1,ptr,isDown)
            # print(node.data,' returns k = ', k+1)
            if node.data == data:
                isDown = False
            if isDown:
                return ptr,k+1,isDown
            return ptr,k-1,isDown
    else:
        # print (node.data,'o','k=',k)
        ptr,k,isDown = nodesAtDistanceK(node.left,data,k,ptr,isDown)
        if ptr != None:
            # print (node.data,'g','k=',k)
            if k == 0:
                # print('h','k=',k)
                print(node.data)
            else:
                # print (node.data,'i','k=',k)
                nodesAtDistanceK(node.right,data,k-1,ptr,isDown)
            return ptr,k-1,isDown
        else:
            # print (node.data,'j','k=',k)
            ptr,k,isDown = nodesAtDistanceK(node.right,data,k,ptr,isDown)
            if ptr != None:
                # print (node.data,'k','k=',k)
                if k == 0:
                    # print('l',end = ' ')
                    print(node.data)
                else:
                    # print (node.data,'m','k=',k)
                    nodesAtDistanceK(node.left,data,k-1,ptr,isDown)
            else:
                return ptr,k,isDown
            
            return ptr,k-1,isDown
    
    
    
# def findNodeAndRoot(root,target):
#     if root == None:
#         return None
#     if root.data == target:
#         return root
    

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

    
def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])
nodesAtDistanceK(root, target, k)
