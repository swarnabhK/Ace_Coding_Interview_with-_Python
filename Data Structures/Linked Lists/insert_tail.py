from LinkedList import LinkedList
from Node import Node

def insert_at_tail(lst,data):
        temp = Node(data)
        if(lst.get_head() is None):
              lst.head = temp
              return
        pointer = lst.get_head()
        while(pointer.next is not None):
            pointer = pointer.next
        pointer.next = temp
        return

lst = LinkedList()
lst.print_list()
insert_at_tail(lst, 0)
lst.print_list()
insert_at_tail(lst, 1)
lst.print_list()
insert_at_tail(lst, 2)
lst.print_list()
insert_at_tail(lst, 3)
lst.print_list()
        