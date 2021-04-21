import Foundation

/*
        Binary Search
        *************
  0 1 2 3 4
 [1,2,3,4,5] target = 5
 O(log n)
 **/

func binarySearch(list: [Int], target: Int) -> Int {
    
    var low = 0
    var high = list.count
    
    while(low <= high) {
        let middle = (low+high)/2
        if(list[middle] == target) {
            return middle
        } else if(list[middle] < target){
            low = middle + 1
        } else {
           high  = middle - 1
        }
    }
    return 0
}

var list = [1,2,3,4,5]
var target = 1
print("Position for \(target) is \(binarySearch(list: list, target: target))")
