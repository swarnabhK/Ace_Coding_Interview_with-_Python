from Node import Node

class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
    def get_head(self):
        return self.head
    def is_empty(self):
        return self.head is None
    
    def print_list(self):
        if(self.is_empty()):
            print("List is empty!")
            return
        temp = self.head
        while(temp.next is not None):
            print(temp.data,end = '->')
            temp = temp.next
        print(temp.data)

