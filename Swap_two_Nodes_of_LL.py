from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapNodes(head, i, j) :
    orighead = head
    beforeA = None
    beforeB = None
    for i in range(i-1):
        head = head.next
        beforeA = head
    head = orighead
    for j in range(j-1):
        head = head.next
        beforeB = head
        
    B = beforeB.next
    if beforeA !=None:
        A = beforeA.next
        beforeA.next = B
    else:
        A = orighead
        orighead = B

        
    afterB = B.next
    afterA = A.next
    
    if i+1 != j:
        B.next = afterA
        beforeB.next = A
    else:
        B.next = A

    
    A.next = afterB
    # print(A.data,afterA.data,beforeB.data,B.data,afterB.data)
    return orighead
    
    
    






























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
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1
