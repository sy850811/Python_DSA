class pqNode:
    def __init__(self,priority,value):
        self.priority = priority
        self.value = value
#1 1 2 1 2 2 1 3 2 1 4 2 1 5 2 1 6 2 1 7 2 1 8 2 1 9 2 1 10 2 -1        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    def isEmpty(self):
        return len(self.pq) == 0
    
    def getSize(self):
        return len(self.pq)

    def getMax(self):
        return self.pq[0].value if not self.isEmpty() else -2147483648
    
    def __percolateUp(self):
        ci = self.getSize() - 1
        
        while ci > 0:
            pi = (ci - 1)//2
            if self.pq[pi].value < self.pq[ci].value :
                self.pq[pi],self.pq[ci] = self.pq[ci],self.pq[pi]
                ci = pi
            else:
                break
                
        
    def insert(self,ele,priority):
        self.pq.append(pqNode(priority,ele))
        self.__percolateUp()
        # print('array-->')
        # [print(i.value,end=' ') for i in self.pq]
        # print()
    
    def __perculateDown(self):
        pi = 0
        
        while 2*pi + 1 < self.getSize():
            min = self.pq[pi]
            cia = 2*pi + 1
            cib = 2*pi + 2
            ci = pi
            if self.pq[cia].value > self.pq[pi].value:
                ci = cia
            if cib < self.getSize():
                if self.pq[cib].value > self.pq[ci].value:
                    ci = cib
            if ci == pi:
                break
            
            self.pq[pi],self.pq[ci] =  self.pq[ci],self.pq[pi]
            
            pi = ci
        
    def removeMax(self):
        if self.isEmpty():
            return -2147483648
        data = self.pq[0].value
        self.pq[0] = self.pq[-1]
        self.pq.pop()
        self.__perculateDown()
        return data
        
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
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
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
