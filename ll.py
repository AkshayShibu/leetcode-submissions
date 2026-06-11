class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def findLowestValue(self,head):
    minval=head.data
    curr=head.next
    while curr:
      if curr.data<minval:
        minval=curr.data
      curr=curr.next
    return minval


  
node1 = Node(1)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

x=node2.findLowestValue(node1)
print("The lowest value in the linked list is:",x )
