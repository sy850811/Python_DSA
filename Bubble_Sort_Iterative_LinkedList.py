from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def bubbleSort(head):
    if head ==None or head.next ==None:
        return head
    orighead = head
    count = 0
    while head != None:
        head = head.next
        count+=1
    count -=1
    
    for i in range(count):
        head = orighead
        prev = None
        while head.next != None:
            # print(head.data)
            if head.data > head.next.data:
                B = head.next
                if prev == None:
                    orighead = B
                else:
                    prev.next = B
                head.next = B.next
                B.next = head
                prev = B
            else:
                prev = head
                head = head.next
        
    return orighead







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
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)
