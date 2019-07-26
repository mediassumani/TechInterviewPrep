
from collections import deque

class TempTracker(object):
    ''' Model records of different temperatures throughout time''' 
    
    def __init__(self):
        
        self.temperatures = {}
        self.high = 0
        self.low = None
        self.size = 0

    def insert(self, degree): # O(1)
        ''' Records a new temperature'''
        
        if self.size == 0:
            self.high = self.low = degree

        if degree > self.high:
            self.high = degree

        elif degree < self.low:
            self.low = degree

        if degree not in self.temperatures:
            self.temperatures[degree] = 1
        else:
            self.temperatures[degree] += 1

        self.size += 1
        

    def get_max(self): # O(1)
        ''' Get the highest temp ever recorded'''
        return self.high
    
    def get_min(self): # O(1)
        ''' Get the lowest temp ever recorded''' 
        return self.low

    def get_mean(self): #(n)
        ''' Get the mean of all the temperatures ever recorded'''
        return sum(self.temperatures.keys()) / self.size/2
    
    def get_mode(self): #(n)
        ''' Get the most frequent temperature recorded '''

        cur_val = 0
        mode = None

        for key,value in self.temperatures.items():
            if value > cur_val:
                cur_val = value
                mode = key

        return mode