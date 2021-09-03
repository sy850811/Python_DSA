from sys import stdin
import sys
sys.setrecursionlimit(15000)
#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def reverseLinkedListRec(head):
    if head == None or head.next == None:
        return head
    subHead = reverseLinkedListRec(head.next)
    head.next.next = head
    head.next = None
    return subHead

def kReverse(head, k) :
    orighead = head
    linkB = head
    first = True
    while linkB != None:
        linkA = head
        for i in range(k-1):
            if head.next == None:
                break
            head = head.next

        linkB = head.next
        head.next = None
        # print(head.data)
        a = reverseLinkedListRec(linkA)
        # printLinkedList(a)
        if first == True:
            orighead = a
            first = False
        else:
            prev.next = head
        linkA.next = linkB
        # if linkB != None:
        #     print(linkA.data , linkB.data)
        head = linkB
        prev = linkA
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
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1
