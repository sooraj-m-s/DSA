class Stack:
   def __init__(self):
       self.data = []
  
   def push(self, data):
       self.data.append(data)
  
   def pop(self):
       if self.data:
           return self.data.pop()
       return 'Stack is empty.'
  
   def peek(self):
       if self.data:
           return self.data[-1]
       return 'Stack is empty.'
  
   def is_empty(self):
       return len(self.data) == 0
  
   def size(self):
       return len(self.data) + 1


stack = Stack()
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(stack.peek())
print(stack.size())


class Queue:
   def __init__(self):
       self.data = []
  
   def enqueue(self, data):
       self.data += [data]
  
   def dequeue(self):
       self.data = self.data[1:]
  
   def peek(self):
       return self.data[0]
  
   def is_empty(self):
       return len(self.head) == 0
  
   def size(self):
       return len(self.head) + 1
  
   def display(self):
       return self.data


q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.display())
q.dequeue()
print(q.display())
