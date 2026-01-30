

#1: Singly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(7)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print(node1) #address print krega
print(node1.data) #data of node1

currentNode = node1
while currentNode:
    print(currentNode.data, end="->")
    currentNode = currentNode.next
print("None")
#but this is not ideal way to immplement linked list




