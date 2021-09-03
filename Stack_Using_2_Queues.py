
from sys import stdin
import queue

class Stack :
    def __init__(self):
        self.a = queue.Queue()
        self.b = queue.Queue()
        self.count = 0
    def getSize(self):
        return self.count
    def isEmpty(self):
        return self.count == 0
    def push(self, data):
        if self.a.qsize() == 0:
            self.b.put(data)
        else:
            self.a.put(data)
        self.count +=1
    def pop(self) :
        
        if self.a.qsize() == 0:
            if self.b.qsize() == 0:
                data = -1
            else:
                for i in range(self.b.qsize() - 1):
                    self.a.put(self.b.get())
                data = self.b.get()
                self.count -=1
        else:
            for i in range(self.a.qsize() - 1):
                self.b.put(self.a.get())
            data = self.a.get()
            self.count -=1
        return data
    def top(self) :
        if self.a.qsize() != 0:
            return self.a.queue[-1]
        else:
            if self.b.qsize() == 0:
                return -1
            else:
                return self.b.queue[-1]
            
		




#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1
