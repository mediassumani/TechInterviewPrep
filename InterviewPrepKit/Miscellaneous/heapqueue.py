import heapq

def create_histogram(arr):
    ''' Creates a key-value pair for an element and its frequency'''
    histogram = {}
    for elem in arr:
        if elem in histogram:
            histogram[elem] += 1
        else:
            histogram[elem] = 1
    return histogram

def get_most_frequent_heapq(arr, n):
    
    histogram = create_histogram(arr) # O(m) where m is the # of elements in arr
    heap = []

    for key,val in histogram.items():
        heapq.heappush(heap, (val,key)) # O(log n)
    return heapq.nlargest(n, heap)

def main():

    colors = ["red", "blue", "red", "yellow", "purple", "blue", "red", "orange", "purple"]
    
    print(get_most_frequent_heapq(colors, 3))

if __name__ == "__main__":
    main()