'''
Traversal of linked list
'''

# Node class
# to create each node of linked list
class Node:
    def __init__(self, info):
        self.info = info  # Assign info
        self.next = None  # point to NULL

# Linked list class
# to hold linked list of nodes
class LinkedList:
    def __init__(self):
        self.head = None  # points to head element

    # display or print contents of list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.info, end=' ')
            temp = temp.next
        print()

def main():

    # create 3 nodes
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)

    # create linked list
    L1 = LinkedList()
    L1.head = first_node
    first_node.next = second_node
    second_node.next = third_node

    # print the list
    L1.printList()

if __name__=='__main__':
    main()
