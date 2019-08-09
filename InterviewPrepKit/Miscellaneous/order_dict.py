
def create_histogram(arr):
    ''' Creates a key-value pair for an element and its frequency'''
    histogram = {}
    for elem in arr:
        if elem in histogram:
            histogram[elem] += 1
        else:
            histogram[elem] = 1
    return histogram

def get_most_frequent_improved(arr, n):

    d = create_histogram(arr) # O(m) where m is the # of elements in arr
    result = []
    count = 0

    for w in sorted(d, key=d.get, reverse=True): #O(n)
        if count == n:
            break
        count += 1
        result.append(w)

    return result