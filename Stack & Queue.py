class Stack:
   def __init__(self):
       self.li = []
  
   def push(self, val):
       self.li.append(val)
  
   def pop(self):
       if self.li:
           return self.li.pop()
       return 'Stack is empty.'
  
   def peek(self):
       if self.li:
           return self.li[-1]
       return 'Stack is empty.'
  
   def size(self):
       print('Size of the Stack is', len(self.li))


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def get_min(self):
        return self.min_stack[-1]


class Queue:
   def __init__(self):
       self.li = []
  
   def enqueue(self, val):
       self.li += [val]
  
   def dequeue(self):
       if self.li:
        self.li = self.li[1:]
  
   def peek(self):
       return self.li[0]
  
   def size(self):
       print("Size of the Queue is", len(self.li))


class PriorityQueue:
    def __init__(self):
        self.li = []
    
    def enqueue(self, priority, val):
        self.li.append([priority, val])
        self.li.sort()
    
    def dequeue(self):
        if self.li:
            self.li = self.li[1:]


class CircularQueue:
    def __init__(self, k):
        self.capacity = k
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQueue(self, value):
        if self.capacity == self.size:
            print("Queue is full")
            return
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def deQueue(self):
        if self.size == 0:
            print("Queue is empty")
            return
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -=1

    def Front(self):
        if self.size == 0:
            print("Queue is empty")
            return
        return self.queue[self.front]

    def Rear(self):
        if self.size == 0:
            print("Queue is empty")
            return
        return self.queue[(self.rear - 1) % self.capacity]

    def isEmpty(self):
        print("Queue is empty" if self.size == 0 else "Queue is not empty")

    def isFull(self):
        print("Queue is full" if self.size == self.capacity else "Queue is not full")




if __name__ == "__main__":
    # Clear the console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    li = [2, 7, 4, 5, 8, 3, 12]

    # Example usage of the data structures
    stack = Stack()
    for i in li:
        stack.push(i)
    # print(stack.pop())
    print(stack.peek())
    stack.size()
    print(stack.li)


    ms = MinStack()
    for i in li:
        ms.push(i)

    print(ms.stack, ms.min_stack)


    q = Queue()
    for i in li:
        q.enqueue(i)
    q.dequeue()
    print(q.li)


    pq = PriorityQueue()
    for i, j in enumerate(li, start=1):
        pq.enqueue(i, j)

    print(pq.li)


    cq = CircularQueue(4)
    cq.enQueue(10)
    cq.enQueue(5)

    print(cq.queue)

