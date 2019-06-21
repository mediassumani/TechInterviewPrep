class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.front = None
        self.rear = None
        self.size = k
        self.counter = 0
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        new_node = Node(value)
        
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.front = self.rear = new_node
            self.rear.next = self.front
            self.counter += 1
            return True
        
        self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front
        self.counter += 1
        return True
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        
        temp = self.front
        if self.isEmpty():
            return False
        
        elif self.front == self.rear:
            self.front = self.rear = None
            self.counter -= 1
            return True
        else:
            
            self.front = self.front.next
            self.counter -= 1
            return True
            
        return False
            

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.front.data
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.rear.data
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        
        return self.front == None and self.rear == None
        
    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.counter == self.size