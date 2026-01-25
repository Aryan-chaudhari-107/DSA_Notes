#1: Structure
class Node:
    def __init__(self, data):
        self.data  = data
        self.next = None
        self.prev = None

class DoubleyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            
            currentNode.next = new_node
            new_node.prev = currentNode

    def inset_at(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_head(data)
            return 

        currentNode = self.head
        count = 0
        while currentNode and count < position:
            currentNode = currentNode.next 
            count += 1

        if currentNode is None:
            print("Postion is out of bounds")
            return 
        
        
        new_node.next = currentNode.next
        new_node.prev = currentNode.prev

        if currentNode.next:
            currentNode.next.prev = new_node
        
        currentNode.next = new_node
    
    def traverse(self):
        currentNode = self.head
        while currentNode.next is not None:
            print(currentNode.data, end="<->")
            currentNode = currentNode.next

    def delete_head(self):
        if self.head is None:
            print("List is empty")
            return 

        temp = self.head
        self.head = self.head.next 
        if self.head:
            self.head.prev = None

        del temp

    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return 
        
        currentNode = self.head
        while currentNode.next is None:
            currentNode.next

        if currentNode.prev:
            currentNode.prev.next = None

        del currentNode

    def delete_at(self, position):
        if self.head is None:
            print("List is empty")
            return 
        
        if position == 0:
            self.delete_head()
            return 
        
        currentNode = self.head
        count = 0

        while currentNode and count < position:
            currentNode = currentNode.next 
            count += 1

        if currentNode is None:
            print("Position is out of bounds")
            return

        if currentNode.next:
            currentNode.next.prev = currentNode
        

    def delete_at(self, position):
        if self.head is None:
            print("List is empty")
            return 
        
        if position == 0:
            self.delete_head()
            return 
        
        currentNode = self.head
        count = 0

        while currentNode and count < position:
            currentNode = currentNode.next 
            count += 1

        if currentNode is None:
            print("Position is out of bounds")
            return

        if currentNode.next:
            currentNode.next.prev = currentNode.prev
        
        if currentNode.prev:
            currentNode.prev.next = currentNode.next

        del currentNode