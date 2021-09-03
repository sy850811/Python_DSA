from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def midPoint(head) :
    slow, fast = head, head
    if head == None:
        return None
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

def add (new,old,head):
    if new == None:
        new = old
        head = old
        old = old.next
    else:
        new.next = old
        new = new.next
        old = old.next
    return new,old,head

def mergeTwoSortedLinkedLists(i, j):
    head = None
    new = None
    while i!=None and j!=None:
        if i.data <= j.data:
            new,i,head = add(new,i,head)
        else:
            new,j,head = add(new,j,head)
    if i == None and j == None:
        return head
    if i!=None:
        if head == None:
            head = i
        else:
        	new.next = i
    elif j!=None:
        if head == None:
            head = j
        else:
        	new.next = j
    return head

def mergeSort(head) :
    if head == None or head.next == None:
        return head
    mid = midPoint(head)
    right = mergeSort(mid.next)
    mid.next = None
    left = mergeSort(head)
    return mergeTwoSortedLinkedLists(right,left)




























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


def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1
