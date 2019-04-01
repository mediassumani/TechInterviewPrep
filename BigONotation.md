
# BigO Notation

### Overview 

In computer science, BigO notation is a way to measure time and space complexity of a given algorithm.

#### O(1) - constant Time

This runtime referes to algorithms that performes at a constant time regardless of the input size.

``` python
def print_name(name):
  print(name)
```

#### O(log n) - Logarithmic Time

This runtime refers to:

* The choice of the next element on which to perform some action is one of several possibilities.
* Only one will need to be chosen.
* The elements on which the action is performed are digits of n.

```python

def binary_search(arr, item):
  ''' 
    Best Case : O(1) if item is in the middle index. 
    Worst Case : O(log n) where n is the size of the array.
  '''
  
  low = 0
  high = len(arr)
  while(low <= high):
    middle = int((low+high)/2)
    if arr[middle] == item:
      return middle
    elif arr[middle] > item:
      high = middle - 1
     else:
      low = middle + 1
```

#### O(n) - Linear Time

This runtime referes to algorithms that performes at a linear time that grows proportionaly with the size of the input.

```python

def linear_search(arr, item):
  ''' 
    Best Case : O(1) if item happens to be at index 1. 
    Worst Case : O(n) where n is the size of arr.
  '''
  return [index for index in arr if arr[index] == item]
```

#### O(n log n) - 


#### O(n^2) - Quadratic Time


#### O(2^n) - 



#### O(n!)
