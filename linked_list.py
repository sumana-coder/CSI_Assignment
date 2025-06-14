class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node to the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print all the nodes in the linked list."""
        if not self.head:
            print("The list is empty.")
            return
        
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index) from the list."""
        if not self.head:
            raise Exception("Cannot delete from an empty list.")
        
        if n <= 0:
            raise IndexError("Index should be a positive integer starting from 1.")

        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        count = 1
        prev = None

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range.")
        
        print(f"Deleting node at position {n} with value {current.data}")
        prev.next = current.next

if __name__ == "__main__":
    ll = LinkedList()
    # Adding elements to the linked list
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Initial list:")
    ll.print_list()

    try:
        ll.delete_nth_node(2)  # Should delete the node with value 20
        print("List after deleting 2nd node:")
        ll.print_list()
        
        ll.delete_nth_node(1)  # Should delete the node with value 10
        print("List after deleting 1st node:")
        ll.print_list()

        ll.delete_nth_node(5)  # Invalid index (out of range)
    except Exception as e:
        print("Error:", e)
