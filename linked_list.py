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
            print(temp.info, end=' -> ')
            temp = temp.next
        print("NULL")

    def insertBeg(self, new_info):
        '''
        Insertion of Node at Beginning
        '''
        new_node = Node(new_info)
        new_node.next = self.head
        self.head = new_node

    def insertAfter_node(self, prev_node, new_info):
        '''
        Insert node after given prev_node, with new_info
        '''
        if prev_node is None:
            self.insertBeg(new_info)
            return
        temp = Node(new_info)
        temp.next = prev_node.next
        prev_node.next = temp

    def insertAfter_info(self, prev_info, new_info):
        '''
        Insert node after given value in a node, with new_info
        '''
        # Linked list traversal
        temp = self.head
        while(temp):
            if temp.info == prev_info:
                self.insertAfter_node(temp, new_info)
                break
            temp = temp.next

    def insertEnd(self, new_info):
        '''
        Insert node at the end of linked list
        '''
        new_node = Node(new_info)
        if self.head is None:
            self.head = new_node
            return

        # Linked list traversal
        temp = self.head
        while(temp.next is not None):
            temp = temp.next

        temp.next = new_node
        
    def deleteInfo(self, info):
        '''
        Delete first occurence of given info
        '''
        temp = self.head
        
        if temp is None:
            return

        # if head node is deleted
        if temp.info == info:
            self.head = temp.next
            temp = None
            return

        # search for info
        # previous node info is stored
        while(temp is not None):
            if temp.info == info:
                break
            prev = temp
            temp = temp.next

        # delete the link
        prev.next = temp.next
        temp = None

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
    print("\nAfter insertion at beginning")
    L1.printList()

    # insert after a given node
    L1.insertAfter_node(second_node, 55)

    # print the list after insertion
    print("\nAfter insertion after 'second_node'")
    L1.printList()

    # insert after a given value
    L1.insertAfter_info(55, 111)

    # print the list after insertion
    print("\nAfter insertion after info 55")
    L1.printList()

    # insert at end
    L1.insertEnd(365)

    # print the list after insertion
    print("\nAfter insertion at end")
    L1.printList()
    
    # Delete info 55
    L1.deleteInfo(55)

    # print the list after deletion
    print("\nAfter deletion 55")

if __name__ == '__main__':
    main()
