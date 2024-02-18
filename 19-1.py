# გაკბვეთილზე გარჩეული დაკავშირებული სიის კოდი გაარჩიე და დააკომენტარე ყოველი
# მნიშვნელოვანი ადგილი. (A single linked list structure)

class ListNode:
    def __init__(self, value):
        # Initialize a node with a given value and a reference to the next node (initially set to None)
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # Initialize a linked list with a head node containing the given value and set length to 1
        self.head = ListNode(value)
        self.length = 1

    def append(self, value):
        # Append a new node with the given value to the end of the linked list
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        new_node = ListNode(value)
        current_node.next = new_node
        self.length += 1

    def insert(self, value, index):
        # Insert a new node with the given value at the specified index
        last_index = self.length - 1
        i = 0

        if index == 0:
            # Insert at the beginning, updating head and length
            old_head = self.head
            self.head = ListNode(value)
            self.head.next = old_head
            self.length += 1

        elif index == last_index + 1:
            # Insert at the end using the append method
            self.append(value)

        elif 0 < index < last_index + 1:
            # Insert in the middle, update next references and length
            current_node = self.head
            while i != index - 1:
                current_node = current_node.next
                i += 1

            new_node = ListNode(value)
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

        elif index > last_index + 1 or index < 0:
            # Handle index out of range
            print("Index is out of range...")

    def remove(self, index):
        # Remove the node at the specified index
        last_index = self.length - 1
        i = 0

        if index == 0:
            # Remove the first node, update head and length
            self.head = self.head.next
            self.length -= 1

        elif index == last_index:
            # Remove the last node, update next reference and length
            current_node = self.head
            while i < last_index - 1:
                current_node = current_node.next
                i += 1

            current_node.next = None
            self.length -= 1

        elif 0 < index < last_index:
            # Remove a node in the middle, update next references and length
            current_node = self.head
            while i != index - 1:
                current_node = current_node.next
                i += 1

            deleted_element = current_node.next
            current_node.next = deleted_element.next
            self.length -= 1

        elif index > last_index + 1 or index < 0:
            # Handle index out of range
            print("Index is out of range...")

    def printList(self):
        # Print the elements of the linked list
        current_node = self.head
        print(f"{current_node.value} ->", end='')
        while current_node.next is not None:
            current_node = current_node.next
            print(f" {current_node.value} ->", end='')

# Example usage:
linked_list = LinkedList(1)
linked_list.append(3)
linked_list.insert(2, 1)
linked_list.append(4)
linked_list.remove(0)
linked_list.printList()
