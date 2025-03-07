class Node:
    """Nodea creation for a DLL"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """Doubly Linked List with insertion, traversal, and length calculation."""
    def __init__(self):
        self.head = None # first node
        self.tail = None # last node

    def length(self):
        count, temp = 0, self.head # Start counter and start from the head
        while temp:
            count += 1
            temp = temp.next # goto next node
        return count

    def insert_head(self, data):
        new_node = Node(data) # create a new node
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head # linking new node to current head 
        self.head.prev = new_node # linking current head back to new node
        self.head = new_node # updating the head to new node

    def insert_tail(self, data):
        new_node = Node(data) # create new node
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node # link last node to new node
        new_node.prev = self.tail # link neaw node back to last node
        self.tail = new_node # update the tail to new node

    def traverse_forward(self):
        temp = self.head # Starting from head
        while temp: # Traverse through the list 
            print(temp.data, end=" <-> ")
            temp = temp.next # keep moving to next node
        print("None") # mark the end of list

    def traverse_backward(self):
        temp = self.tail # Starting from tail
        while temp: # Traverse through the list but backwards
            print(temp.data, end=" <-> ")
            temp = temp.prev # keep moving to previous node
        print("None") # Mark the start of the list

# -------------------
# TEST CASES
# -------------------
# if __name__ == "__main__":
#     dll = DoublyLinkedList()

#     # Case 1: Insert at head
#     dll.insert_head(10)
#     dll.insert_head(20)
#     dll.insert_head(30)

#     print("Forward Traversal:")
#     dll.traverse_forward()  # Output: 30 <-> 20 <-> 10 <-> None

#     print("\nBackward Traversal:")
#     dll.traverse_backward()  # Output: 10 <-> 20 <-> 30 <-> None

#     print("\nLength of List:", dll.length())  # Output: 3

#     # Case 2: Insert at tail
#     dll.insert_tail(40)
#     dll.insert_tail(50)

#     print("\nForward Traversal after inserting at tail:")
#     dll.traverse_forward()  # Output: 30 <-> 20 <-> 10 <-> 40 <-> 50 <-> None

#     print("\nBackward Traversal after inserting at tail:")
#     dll.traverse_backward()  # Output: 50 <-> 40 <-> 10 <-> 20 <-> 30 <-> None

#     print("\nLength of List after inserting at tail:", dll.length())  # Output: 5
