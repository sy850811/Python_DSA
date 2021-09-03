
from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack() :
    def __init__(self):
        self.head = None
        self.count = 0
        



    '''----------------- Public Functions of Stack -----------------'''


    def getSize(self) :
        #Implement the getSize() function
        return self.count



    def isEmpty(self) :
        #Implement the isEmpty() function
        return self.count == 0



    def push(self, data) :
        #Implement the push(element) function
        n = Node(data)
        n.next = self.head
        self.head = n
        self.count+=1



    def pop(self) :
        #Implement the pop() function
        if self.head == None:
            # print("Nothing to pop from the stack as it is empty")
            return -1
        else:
            a= self.head.data
            self.head = self.head.next
            self.count-=1
            return a



    def top(self) :
        #Implement the top() function
        if self.head == None:
            # print("The stack as it is empty")
            return -1
        else:
            return self.head.data
        




#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.getSize())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1
