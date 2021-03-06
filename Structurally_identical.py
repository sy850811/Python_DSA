from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(root1, root2):
    if root1==None and root2 ==None:
        return True
    if root1.data != root2.data:
        return False
    if len(root1.children) != len(root2.children):
        return False
    for i in range(len(root1.children)):
        c1 = root1.children[i]
        c2 = root2.children[i]
        
        if c1.data != c2.data:
            return False
        if not isIdentical(c1,c2):
            return False
    return True
        





def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr1 = list(int(x) for x in stdin.readline().strip().split())
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in stdin.readline().strip().split())
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')
