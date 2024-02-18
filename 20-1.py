class Node:
    def __init__(self, key):
        """
        Initialize a new Node with a given key.

        Args:
        - key: The value associated with the node.
        """
        self.key = key
        self.left = None  # Pointer to the left child node
        self.right = None  # Pointer to the right child node


class BinaryTree:
    def __init__(self):
        """
        Initialize an empty binary tree.
        """
        self.root = None  # Pointer to the root node

    def insert(self, key):
        """
        Insert a new key into the binary tree.

        Args:
        - key: The value to be inserted.
        """
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        """
        Helper method for recursive insertion.

        Args:
        - root: The current root node.
        - key: The value to be inserted.

        Returns:
        The updated root node.
        """
        if root is None:
            # If the tree is empty or we reach a leaf node, create a new node
            return Node(key)
        
        # Recursively insert the key based on comparison
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)

        return root

    def inorder_traversal(self, root):
        """
        Perform an inorder traversal of the binary tree.

        Args:
        - root: The root node from which traversal begins.
        """
        if root:
            # Traverse the left subtree
            self.inorder_traversal(root.left)
            
            # Visit the current node
            print(root.key, end=" ")
            
            # Traverse the right subtree
            self.inorder_traversal(root.right)


# Example usage:
if __name__ == "__main__":
    # Create a binary tree instance
    binary_tree = BinaryTree()

    # Insert values into the binary tree
    keys_to_insert = [5, 3, 7, 2, 4, 6, 8]
    for key in keys_to_insert:
        binary_tree.insert(key)

    # Perform an inorder traversal and print the result
    print("Inorder Traversal:")
    binary_tree.inorder_traversal(binary_tree.root)
