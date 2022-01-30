'''
LINKED LIST
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

    def printList(self):
        '''
        Traversal of linked list
        '''
        temp = self.head
        while(temp):
            print(temp.info, end=' ')
            temp = temp.next
        print()

    def insertBeg(self, info):
        '''
        Insertion of Node at Beginning
        '''
        new_node = Node(info)
        new_node.next = self.head
        self.head = new_node

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

    # insert at beginning
    L1.insertBeg(100)

    # print the list after insertion
    print("\nAfter insertion")
    L1.printList()

if __name__ == '__main__':
    main()
