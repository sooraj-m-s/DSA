# def get_fac(x):
#     if x <= 1:
#         return x
#     return x * get_fac(x-1)

# print(get_fac(5))


li = [1, 3, 4, 5, 6, 9, 11, 15, 18, 21, 25]
target_element = 15

l = 0
u = len(li) - 1

while l <= u:
    mid = (l+u) // 2

    if li[mid] == target_element:
        mid + 1
        break
    elif li[mid] < target_element:
        l = mid + 1
    else:
        u = mid - 1


print(f'Value {target_element} found position {mid}')



# class Singly:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def printLL(self):
#         if self.head is None:
#             print('Linked list is empty.')
#             return
        
#         n = self.head
#         while n is not None:
#             print(n.data, '-->', end=' ')
#             n = n.next

#     def insert(self, data):
#         if self.head is None:
#             self.head = Singly(data)
#             return
#         new_node = Singly(data)
#         new_node.next = self.head
#         self.head = new_node

# l = LinkedList()
# l.insert(1)
# l.insert(2)
# l.insert(3)
# l.insert(4)
# l.printLL()
