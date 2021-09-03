class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
        
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
    
    def __perculateDown(self):
        parentIndex = 0
        while 2*parentIndex + 1 < self.getSize():
            childIndexA = (2*parentIndex + 1)
            if childIndexA != self.getSize() -1:
                childIndexB = (2*parentIndex + 2)
                smallestChild = childIndexA if self.pq[childIndexA].priority < self.pq[childIndexB].priority else childIndexB
            else:
                smallestChild = childIndexA
            
            if self.pq[smallestChild].priority < self.pq[parentIndex].priority:
                self.pq[smallestChild],self.pq[parentIndex] = self.pq[parentIndex],self.pq[smallestChild]
                parentIndex = smallestChild
            else:
                break
	
#     def __perculateDown(self):
#         pi = 0
#         lc = 2*pi+1
#         rc = 2*pi+2
#         while lc<self.getSize():
#             mi = pi
#             if self.pq[lc].priority<self.pq[mi].priority:
#                 mi = lc
                
#             if rc<self.getSize() and self.pq[rc].priority<self.pq[mi].priority:
#             	mi = rc
#             if mi==pi:
#                 break
#             self.pq[mi],self.pq[pi] = self.pq[pi],self.pq[mi]
#             pi = mi
#             lc = 2*pi+1
#             rc = 2*pi+2
        
            
    def removeMin(self):
        if self.isEmpty():
            return None
        returnValue = self.pq[0].ele
        self.pq[0] = self.pq[-1]
        # del self.pq[-1]
        self.pq.pop()
        self.__perculateDown()
        return returnValue
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
        
    
