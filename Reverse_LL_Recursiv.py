from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



# def reverseLinkedListRec(curr,prev=None) :
#     if curr == None:
#         return prev
#     elif curr.next == None:
#         curr.next = prev
#         return curr
    
#     x= reverseLinkedListRec(curr.next,curr)
#     curr.next = prev
#     return x
	
def reverseLinkedListRec(head):
    if head == None or head.next == None:
        return head
    subHead = reverseLinkedListRec(head.next)
    head.next.next = head
    head.next = None
    return subHead





























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

    newHead = reverseLinkedListRec(head)
    printLinkedList(newHead)

    t -= 1
