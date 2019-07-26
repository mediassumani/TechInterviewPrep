
from collections import deque

class TempTracker(object):
    ''' Model records of different temperatures throughout time''' 
    
    def __init__(self):
        
        self.temperatures = {}
        self.high = 0
        self.low = None
        self.size = 0

    def insert(self, degree):
        ''' Records a new temperature'''
        
        if self.size == 0:
            self.high = self.low = degree

        if degree > self.high:
            self.high = degree

        elif degree < self.low:
            self.low = degree
        

    def get_max(self):
        return self.high
    
    def get_min(self):
        return self.low


    def get_mean(self):
        pass
    
    def get_mode(self):
        pass