#1: singly circlular linked list:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            currentNode = self.head
            while currentNode.next != self.head:
                currentNode = currentNode.next
            currentNode.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            print(currentNode.data, end="->")
            currentNode = currentNode.next
            if currentNode == self.head:
                break
        print("(head)") 

#2: dobly circular linked list:
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if not self.head:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            print(currentNode.data, end="<->")
            currentNode = currentNode.next
            if currentNode == self.head:
                break
        print("(head)")