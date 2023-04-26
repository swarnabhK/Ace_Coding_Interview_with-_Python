from LinkedList import LinkedList
from Node import Node
from insert_tail import insert_at_tail,lst


def search(lst,value):
    temp = lst.head
    while(temp):
        if(temp.data==value):
            return str(value)+" has been found"
        temp = temp.next
    return str(value)+" is not present in the linked list"


print("Importing the list already initialized in insert_tail file")
lst.print_list()
print(search(lst,3))
print(search(lst,4))

