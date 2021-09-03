from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    if head == None:
        return head
    
    evenhead,even,oddhead,odd = None,None,None,None

    while head != None:
        
        if head.data % 2 == 0:
            if even == None:
                even = head
                evenhead = head
            else:
                even.next = head
                even = even.next
        else:
            if odd == None:
                odd = head
                oddhead = head
            else:
                odd.next = head
                odd = odd.next
                
        head = head.next

    
    if oddhead == None:
        even.next = None
        return evenhead
    else:
        if even == None:
            odd.next = None
        else:
            odd.next = evenhead
            even.next = None
        return oddhead
























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
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1
