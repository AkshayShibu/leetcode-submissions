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

def deleteSpecificNode(head, key):
  if head and head.data==key:
    return head.next
  else:
    curr=head
    while curr.next:
      if curr.next.data==key:
        curr.next=curr.next.next
      curr=curr.next
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)   
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1,2)

print("\nAfter deletion:")
traverseAndPrint(node1)
