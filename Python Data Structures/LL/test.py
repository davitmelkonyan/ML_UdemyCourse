from SinglyLL import Node
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
print (a.value)
print (a.next.value)

from DoublyLL import DoublyLLNode
a1 = DoublyLLNode(1)
b1 = DoublyLLNode(2)
c1 = DoublyLLNode(3)
a1.next = b1
b1.prev = a1
b1.next = c1
c1.prev = b1