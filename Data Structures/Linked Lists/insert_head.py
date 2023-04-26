from LinkedList import LinkedList
from Node import Node

def insert_at_head(lst,data):
    temp = Node(data)
    temp.next = lst.head
    lst.head = temp
    return

list = LinkedList()
list.print_list()
print(list.get_head())
print(list.is_empty())

print("Inserting values in the list")
for i in range(1,10):
    insert_at_head(list,i)
list.print_list()