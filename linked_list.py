class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print('Linked List is empty.')
            return
        n = self.head
        while n is not None:
            print(n.data, '-->', end=' ')
            n = n.next

    def insert_empty(self, data):
        if self.head is not None:
            print('Linked list is not empty')
            return
        self.head = SinglyNode(data)
        
    def add_begin(self, data):
        new_node = SinglyNode(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = SinglyNode(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def add_after(self, data, x):
        if self.head is None:
            print('Linked list is empty')
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print(f'Entered value {x} is not found in the Linked List.')
            return
        new_node = SinglyNode(data)
        new_node.next = n.next
        n.next = new_node

    def add_before(self, data, x):
        if self.head is None:
            print('Linked list is empty')
            return
        new_node = SinglyNode(data)
        if self.head.data == x:
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print(f'Entered value {x} is not found in the Linked List.')
            return
        new_node.next = n.next
        n.next = new_node

    def del_begin(self):
        if self.head is None:
            print('Linked list is empty')
            return
        self.head = self.head.next

    def del_end(self):
        if self.head is None:
            print('Linked list is empty')
            return
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None

    def del_value(self, x):
        if self.head is None:
            print('Linked list is empty')
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print(f'Entered value {x} is not in the Linked list.')
            return
        n.next = n.next.next

    def get_count(self):
        cnt = 0
        n = self.head
        while n is not None:
            cnt += 1
            n = n.next
        return cnt
    
    def del_center(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
    
    def reverseLL(self):
        if self.head.next is None:
            print('Need atleast 2 data to reverse!')
        else:
            n = self.head
            prev = None
            while n is not None:
                new = n.next
                n.next = prev
                prev = n
                n = new
            self.head = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head is None:
            print('Linked list is empty')
            return
        n = self.head
        while n.nref is not None:
            print(n.data, '-->', end=' ')
            n = n.nref
        print(n.data)
        print('\nReverse')
        while n is not None:
            print(n.data, '-->', end=' ')
            n = n.pref

    def add_begin(self, data):
        if self.head is None:
            self.head = DoublyNode(data)
        else:
            new_node = DoublyNode(data)
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self, data):
        if self.head is None:
            self.head = DoublyNode(data)
        else:
            new_node = DoublyNode(data)
            n = self.head
            while n.nref is not None:
                n = n.nref
            new_node.pref = n
            n.nref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            new_node = DoublyNode(data)
            if self.head.data == x:
                new_node.nref = self.head
                self.head.pref = new_node
                self.head = new_node
                return
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print(f'Entered valure {x} is not in the linked list')
                return
            new_node.nref = n.pref.nref
            new_node.pref = n.pref
            n.pref.nref = new_node
            n.pref = new_node

    def add_after(self, data, x):
        if self.head is None:
            print('Linked list is empty')
            return
        n = self.head
        new_node = DoublyNode(data)
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print(f'Entered valure {x} is not in the linked list')
            return
        if n.nref is None:
            n.nref = new_node
            new_node.pref = n
            return
        new_node.pref = n
        new_node.nref = n.nref
        n.nref.pref = new_node
        n.nref = new_node

    def del_first(self):
        if self.head is None:
            print('Linked list is empty')
            return
        if self.head.nref is None:
            self.head = None
            return
        self.head.nref.pref = None
        self.head = self.head.nref

    def del_last(self):
        if self.head is None:
            print('Linked list is empty')
            return
        if self.head.nref is None:
            self.head = None
            return
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    def del_value(self, x):
        if self.head is None:
            print('Linked list is empty')
            return
        if self.head.data == x and self.head.nref is None:
            self.head = None
        elif self.head.data == x:
            self.head.nref.pref = None
            self.head = self.head.nref
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.nref
        if n is None:
            print(f'Entered valure {x} is not in the linked list')
            return
        if n.nref is None:
            n.pref.nref = None
            return
        n.pref.nref = n.nref
        n.nref.pref = n.pref




if __name__ == '__main__':
    # Clear the console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # Test Singly and Doubly Linked List
    sll = SinglyLinkedList()
    sll.insert_empty(1)
    sll.add_begin(2)
    sll.add_begin(4)
    sll.add_end(3)

    sll.add_after(4, 3)
    sll.add_before(8, 1)
    sll.del_begin()
    sll.del_end()
    sll.del_value(6)
    sll.del_center()
    sll.reverseLL()

    sll.print_LL()
    print(f'\nLinked list have {sll.get_count()} data')


    dll = DoublyLinkedList()
    dll.add_begin(4)
    dll.add_begin(5)
    dll.add_begin(6)
    dll.add_end(3)
    dll.add_end(2)
    dll.add_end(1)

    dll.add_before(0, 4)
    dll.add_after(0, 2)
    dll.del_first()
    dll.del_last()
    dll.del_value(1)

    dll.printLL()

