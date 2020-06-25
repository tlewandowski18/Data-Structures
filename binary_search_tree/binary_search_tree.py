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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #compare new value to current value of node
        #passed value is less than or equal to node's value
        if value < self.value:
            #if there is no left child for Node, insert the value as the left child
            if self.left is None:
                self.left = BSTNode(value)
            #if there is a left child for Node, call the insert function on that Node
            else:
                self.left.insert(value)
        #passed value is greater than the node's value    
        else:
            #if there is no right child for Node, insert the value as the right child
            if self.right is None:
                self.right = BSTNode(value)
            #if there is a right child for Node, call insert on that Node
            else:
                self.right.insert(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check if target is equal to current_value
        if self.value == target:
            return True
        #if target is less than current_value
        elif target < self.value:
            #return false if there is no value less than current value in the tree
            if self.left is None:
                return False
            #if there is a value less than current value, run "contains" on the node containing that value
            return self.left.contains(target)
        #if target is greater than current_value
        else:
            #return false if there is no value greater than current value in the tree
            if self.right is None:
                return False
            #if there is a value less than current value, run "contains" on the node containing that value
            return self.right.contains(target)
        
        

    # Return the maximum value found in the tree
    def get_max(self):
        #check to see if current node has a right child
        #if no right child return value of current node
        if self.right is None:
            return self.value
        #if right child run "get_max on right child"
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #call function on node of root value
        fn(self.value)
        #if root has a left child, re-run for_each on that child
        if self.left:
            self.left.for_each(fn)
        #if root has a right child, re-run for_each on that child
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
