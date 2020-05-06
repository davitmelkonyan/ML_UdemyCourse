#Given 1st node, find if LL contains a "cycle"
from SinglyLL import Node

def cycle_check(node):
    repeated = []
    while node.next != None:
        if(node.next in repeated):
            return False
        else:
            repeated.append(node.value)

    return True