
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




def printIthNode(headm, i,data):
    head = headm
    count = 0
    prev = None
    try:
        while count != i:
            prev = head
            head = head.next
            count +=1
        print(prev.data)
    except AttributeError:
        print()
    n = Node(data)
    if prev == None:
        n.next = headm
        headm = n
    n.next = prev.next
    prev.next = n
    
    printLinkedList(headm)
    


























#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    i = int(stdin.readline().rstrip())
    printIthNode(head, i,555)

    t -= 1
