#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Node counter initialized to zero
        node_count = 0
        # Start at the head node
        node = self.head
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:
            # Count one for this node
            node_count += 1
            # Skip to the next node
            node = node.next
        # Now node_count contains the number of nodes
        return node_count

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) if the index is the head's or tail's
        Worst case running time: O(n) if the index is right before the tail"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        # set a conter to keep track of which index we are on
        curr_index = 0
        curr_node = self.head

        # Return the data at the head if the given index is the first
        if index == 0:
            return self.head.data
        # Return the data at the tail if the given index is the last
        if index == self.size:
            return self.tail.data

        while curr_node is not None:
            if curr_index == index :
                # return the node's data if the counter is equivalent to the index
                return curr_node.data

            # increment the counter and shift to the next node
            curr_index += 1
            curr_node = curr_node.next

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) if the index is the head's or tail's
        Worst case running time: O(n) if the index is right before the tail"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        
        # Prepending the element since the index is refering to the 0th position
        if index == 0:
            self.prepend(item)
            return
        # Appending the element since the index is equivalent to the size of the ll
        if index == self.size:
            self.append(item)
            return

        # Creating pointers to re-arrange nodes in the linkedlist
        new_node = Node(item)
        curr_node = self.head
        curr_index = 0
        # traverse linkedlist from current
        while curr_node is not None:
            # checks if we are one node behind the target node
            if (curr_index + 1 == index):
                temp = curr_node.next # set temp to the current's next node
                curr_node.next = new_node # set current's next node to the new node
                new_node.next = temp # set the new node's next to temp
                self.size += 1 # increment the size since we are inserting an element
                return 

            curr_node = curr_node.next
            curr_index += 1

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) if the ll is empty or has elements"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
            self.size += 1
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
            self.size += 1
        # Update tail to new node regardless
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time:O(1) if the ll is empty or has elements"""
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
            self.size += 1
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
            self.size += 1
        # Update head to new node regardless
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: O(1) if old_item is contained on head or tail node
        Worst case running time: O(n) if the old_item is contained before the tail"""
        
        # Replace the head's data to the new one if it matches the old_item
        if self.head.data == old_item:
            self.head.data = new_item
            return
        # Replace the tail's data to the new one if it matches the old_item
        if self.tail.data == old_item:
            self.tail.data = new_item
            return

        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == old_item:
                # Replace the current's node data if it matches old_item
                curr_node.data = new_item
                return 

            curr_node = curr_node.next

        raise ValueError('{} Not in LinkedList'.format(new_item))
            
    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if the the list is empty.
        Worst case running time: O(n) if the node to be delete is right before the tail"""
        # Start at the head node
        node = self.head
        # Keep track of the node before the one containing the given item
        previous = None
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                previous = node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                previous.next = node.next
                # Unlink the found node from its next node
                node.next = None
                self.size -= 1
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                # Unlink the found node from the next node
                node.next = None
                self.size -= 1
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if previous is not None:
                    # Unlink the previous node from the found node
                    previous.next = None
                    self.size -= 1
                # Update tail to the previous node regardless
                self.tail = previous
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()