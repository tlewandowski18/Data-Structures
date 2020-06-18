#data_structures
    # Need to access data
    # Need to add data to the structure
    # Need to be able to delete data
    # We may need to search through a data structure

#linked_lists
    # Values are linked to each other and know how to get to next one
    # Each node knows how to get to the next one

class Node:
    def __init__(self, value=None, next_node=None):
        self.value= value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None #stores a node that corresponds to our first node in list
        self.tail = None # stores a node that is the end of the list

    def add_to_head(self, value):
        #create a node to add
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def add_to_tail(self, value):
        #create a node to add
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value


    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False


linked_list = LinkedList()

linked_list.add_to_head(0)
linked_list.add_to_tail(1)

print(f'does our LL contain 0? {linked_list.contains(0)}')
print(f'does our LL contain 1? {linked_list.contains(1)}')
print(f'does our LL contain 2? {linked_list.contains(2)}')

linked_list.add_to_head(2)
print(f'Head value: {linked_list.head.value}')
linked_list.add_to_head(5)
print(f'Head value: {linked_list.head.value}')
linked_list.remove_head()
print(f'Head value: {linked_list.head.value}')