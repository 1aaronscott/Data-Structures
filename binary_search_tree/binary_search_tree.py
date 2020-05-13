"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BinarySearchTree:
    ''' implement a bst '''

    def __init__(self, value):
        self.value = value  # root node created when object instantiated
        self.left = None
        self.right = None

    def insert(self, value):
        ''' Insert the given value into the tree '''
        # if value to insert is greater than current node, go right
        # in a prior cohort's video the instructor said put dupe values
        # on the right so using a <= here
        if self.value <= value:
            # is there is no right node, make one
            if self.right is None:
                self.right = BinarySearchTree(value)
            # otherwise treat the node as the start of a new tree
            else:
                self.right.insert(value)
        # reverse of the "go right" logic above
        if self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        ''' Traverses the tree to find the input target variable '''
        if self.value == target:
            return True
        # target is larger the current node, go right
        if self.value < target:
            if self.right is None:  # but there is no right so the target isn't here
                return False
            else:  # go right and make it the current node
                return self.right.contains(target)
        else:  # reverse of the "go right" logic above
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    def get_max(self):
        ''' Return the maximum value found in the tree '''
        # does root have a right node? n=root is max, y=right is current
        # current is new root so recurse
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, fn):
        ''' Call the function `fn` on the value of each node '''
        # run the function on the current node
        fn(self.value)
        # if there's a right node, run the function on it
        # this will take care of all rights
        if self.right:
            self.right.for_each(fn)
        # similarly for any left nodes
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    def in_order_print(self, node):
        ''' Print all the values in order from low to high
        Hint:  Use a recursive, depth first traversal '''
        if node is None:
            return None
        print(node.value)
        if self.left:
            self.left.in_order_print(node.left)
        if self.right:
            self.right.in_order_print(node.right)

    def bft_print(self, node):
        ''' Print the value of every node, starting with the given node,
        in an iterative breadth first traversal '''
        pass

    def dft_print(self, node):
        ''' Print the value of every node, starting with the given node,
        in an iterative depth first traversal '''
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
