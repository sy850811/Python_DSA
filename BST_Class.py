class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self,root):
        if root == None:
            return
        print(root.data,end=':')
        if root.left != None:
            print('L:' + str(root.left.data),end=',')
        if root.right != None:
            print('R:'+str(root.right.data),end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
        
        
    def printTree(self):
        self.printTreeHelper(self.root)
    
    def searchHelper(self,root,data):
        if root == None:
            return False
        if root.data == data:
            return True
        if data < root.data:
            return self.searchHelper(root.left,data)
        return self.searchHelper(root.right,data)
    
    
    def search(self, data):
        return self.searchHelper(self.root,data)

    def insertHelper(self,root,data):
        if root == None:
            return BinaryTreeNode(data)
        if data <= root.data:
            root.left = self.insertHelper(root.left,data)
        else:
            root.right =  self.insertHelper(root.right,data)
        return root
        
    def insert(self, data):
        ptr = self.insertHelper(self.root,data)
        if self.root == None:
            self.root = ptr
            self.numNodes += 1

    def pickSmallestFromRightSubTree(self,root):
        if root.left == None:
            return root.right,root
        root.left,e = pickSmallestFromRightSubTree(root.left)
        return root,e
        
        
    def deleteHelper(self,root,data):
        if root == None:
            return root
        if root.data == data:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            
            a,node = self.pickSmallestFromRightSubTree(root.right)
            node.left = root.left
            if root.right == node:
                node.right == None
            else:
                node.right = root.right
            return node
        root.left = self.deleteHelper(root.left,data)
        root.right = self.deleteHelper(root.right,data)
        return root
    
    def delete(self, data):
        self.root = self.deleteHelper(self.root,data)
    
    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()
