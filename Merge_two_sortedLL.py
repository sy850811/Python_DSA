from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


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


# Main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head1 = takeInput()
    head2 = takeInput()

    newHead = mergeTwoSortedLinkedLists(head1, head2)
    printLinkedList(newHead)

    t -= 1
