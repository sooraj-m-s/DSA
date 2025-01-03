from linked_list import SinglyLinkedList, DoublyLinkedList

# sll = SinglyLinkedList()
# sll.insert_empty(1)
# sll.add_begin(2)
# sll.add_begin(4)
# sll.add_end(3)

# sll.add_after(4, 3)
# sll.add_before(8, 1)
# sll.del_begin()
# sll.del_end()
# sll.del_value(6)
# sll.del_center()
# sll.reverseLL()

# sll.print_LL()
# print(f'\nLinked list have {sll.get_count()} data')


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
