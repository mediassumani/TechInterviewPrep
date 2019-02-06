class Node(object):

    def __init__(self, data=None):
        self.next = None
        self.data = data

class Stack(object):

    def __init__(self, iterable=None):
        self.top = None
        self.size = 0
        self.max = 0

        if iterable is not None:
            for item in iterable:
                self.push(item)

    #O(1)
    def isEmpty(self):
        return self.top is None

    # O(1)
    def push(self, item):

        node = new Node(item)
        if self.isEmpty():
            self.top = node
            self.size += 1

        if item > self.max:
            self.max = item

        node.next = self.top
        self.top = node
        self.size += 1

    # O(n) if we are poping the max value
    # O(1) if we are not poping the max value
    def pop(self):

        if self.isEmpty():
            return

        data = self.top.data
        self.size -= 1

        if self.top.next:

            # checks if we're poping the max value
            if self.top.data == self.max:
                curr = self.top.next
                while curr:
                    if curr.data >= self.max:
                        self.max = self.curr.data
            else:
                self.top = self.top.next
        else:
            self.top = None
            sel.max = 0
        return data

    #O(1)
    def peek():
        if self.isEmpty():
            return
        else:
            return self.top.data

    # O(1)
    def max(self):
        return self.max
