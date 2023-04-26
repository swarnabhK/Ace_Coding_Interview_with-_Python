from LinkedList import LinkedList
from Node import Node
from insert_tail import insert_at_tail


def delete_at_head(lst):
    curr = lst.get_head()
    if(curr is not None):  
      lst.head = curr.next
      curr.next = None
    return

list = LinkedList()
print("Inserting values into the linked list inside delete")

for i in range(1,10):
   insert_at_tail(list,i)

list.print_list()
delete_at_head(list)
print("List after deleting the head element")
list.print_list()
delete_at_head(list)
print("List after deleting the head element")
list.print_list()