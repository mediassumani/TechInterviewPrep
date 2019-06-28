
# BigO Notation

## Overview 

In computer science, BigO notation is a way to measure time and space complexity of a given algorithm. These are my notes from Gayle Laakmann's Cracking The Coding Interview and other resources.

## Time Complexity(runtime)

### O(1) - constant Time

This runtime referes to algorithms that performes at a constant time regardless of the input size.

``` python
def print_name(name):
  print(name)
```
NOTE : The algorithm above is constant time because that's roughly how long it takes for the compiler to print to the standard outpout. Other common O(1) operations are:

* Assigning a variable
* Conditional statement (if, else)
* Returning a value

### O(log n) - Logarithmic Time

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

<bold>NOTE</bold>: The runtime of a recursive funtion with multiple branches is typically O(branches^ depth)

### O(n) - Linear Time

This runtime referes to algorithms that performes at a linear time that grows proportionaly with the size of the input.

```python

def linear_search(arr, item):
  ''' 
    Best Case : O(1) if item happens to be at index 1. 
    Worst Case : O(n) where n is the size of arr.
  '''
  return [index for index in arr if arr[index] == item]
```

### O(n log n) - 
This runtime refers to algorithms that does an O(log n) operations n amount of times. 

```python

def two_sum(arr, target):

  sorted_arr = sorted(arr)
  for num in sorted_arr: O(n)
    other_val = target - num
    index_other_val = binary_searh(arr, other_val) # Binary search is O(log n)
    if index_other_val:
      return [num, arr[index_other_val]]
```

### O(n^2) - Quadratic Time

This runtime referes to algorithms that performe a certain computation N squared times where N is a given size of the input.

```python

def stuff(arrOne, arrTwo):
  
  for i in arrOne:
    for j+1 in arrTwo:
      print(j)
```

### O(2^n) - 



### O(n!)


## Space Complexity 

This refers to the largest size of memory that can be used at runtime of an algorithm.
