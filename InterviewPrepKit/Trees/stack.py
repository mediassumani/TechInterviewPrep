#!python

from  linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Since the LinkedList's prepend fnution is constant time"""

        self.list.prepend(item)
        
    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty.
        Running Time: O(1) since we are just grabbing the head's data
        """

        if self.list.is_empty() is True:
            return None
        
        return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Since getting the head from the the ll is constant time"""
        
        # Raises an error if trying to pop from an empty stack
        if self.list.is_empty() is True:
            raise ValueError("Cannot pop element from empty stack")

        else:
            # grab the item that must be returned from the top/head
            target_item = self.list.head.data
            if self.list.head:
                # Unlink and Shift the top/head one node down on the stack
                self.list.head = self.list.head.next
            else:
                # Nullify the top/head since we've already gotten its value
                self.list.head = None

        # Update the size of the stack and return the item from the top
        self.list.size -= 1
        return target_item


class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        count = 0
        for _ in self.list:
            count += 1

        return count

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) since we are just adding an element at the top of the stack"""

        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        
        if self.is_empty():
            return None
        
        return self.list[self.length() - 1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) since we are removing the last element"""

        if self.is_empty():
            raise ValueError("Stack is Empty")

        return self.list.pop(self.length()-1)


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
