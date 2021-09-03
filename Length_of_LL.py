
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None






def length(head) :
    count = 0
    while head is not None:
        count+=1
        head = head.next
    return count











        




#Taking Input Using Fast I/O
# def takeInput() :
#     head = None
#     tail = None

#     datas = list(map(int, stdin.readline().rstrip().split(" ")))

#     i = 0
#     while (i < len(datas)) and (datas[i] != -1) :
#         data = datas[i]
#         newNode = Node(data)

#         if head is None :
#             head = newNode
#             tail = newNode

#         else :
#             tail.next = newNode
#             tail = newNode

#         i += 1

#     return head

def takeInput():
    head = None
    tail = None
    data = [int(i) for i in input().split()]
    for i in data:
        node = Node(i)
        if(head == None):
            head = node
            tail = node
            continue
        tail.next = node
        tail = node
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
    print(length(head))

    t -= 1
