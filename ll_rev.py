class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  
  print("null")

def rev(head):
  l=[]
  curr=head
  while curr and curr is not None:
    l.append(curr.val)
  for i in range(len(l)):
    print(l[i])

node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2

node1 = rev(node1)
rev(node1)

print("\nAfter insertion:")
traverseAndPrint(node1)
