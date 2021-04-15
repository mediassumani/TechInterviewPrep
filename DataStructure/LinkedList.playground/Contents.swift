import Foundation

/*
    * A LinkedList is a Linear data structure that dynamically changes its size, unlike an array. A LinkedList is made up of nodes, and a node is made up of its data and a reference to the subsequent node.
 
    * The first node of a LinkedList is called head.
    *
 */

class LinkedListNode{
    
    var data: Int?
    var next: LinkedListNode?
    
    init(data: Int? = nil) {
        self.data = data
    }
}

class LinkedList {
    
    var head: LinkedListNode?
    var size = 0
    
    init() {
        self.head = nil
    }

    /*
        Prints the LinkedList into a nice format. Time Complexity: O(1) if list empty, O(n) where n is the # of elements in the list
     */
    func prepttyPrint() {

        var array = [Int]()
        if (self.isEmpty()) {
            print("LinkedList is Empty")
            return
        } else {
            var temp = self.head
            while(temp != nil){
                array.append(temp?.data ?? 0)
                temp = temp?.next
            }
        }
        print(array)
    }
    
    /*
        Adds an element at the end of the LinkedList. Time Complexity: O(1) if list empty, O(n) where n is the # of elements in the list
     */
    func append(data: Int) {
        
        // The node that must be inserted into the end of the linkedlist
        let newNode = LinkedListNode(data: data)
        
        // Assign the head to become the new node if the list is empty + increase the size by one
        if(self.isEmpty()) {
            self.head = newNode
            self.size += 1
        } else {
            // Create a "holder" node that can be use to keep reference over each iterated node in the list
            var currentNode = self.head
            while(currentNode?.next != nil) {
                // Increase the position of the current node in the list sequentially until we get to the end
                currentNode = currentNode?.next
            }
            // Once the current node reaches the end, assign the new node as its next + increment the size by 1
            currentNode?.next = newNode
            self.size += 1
        }
    }
    
    /*
        Adds an element at the beginning of the LinkedList. Time Complexity: O(1).
     */
    func prepend(data: Int) {
        
        let newNode = LinkedListNode(data: data)
        if (self.isEmpty()) {
            self.head = newNode
            self.size += 1
        } else {
            newNode.next = self.head
            self.head = newNode
            self.size += 1
        }
    }
    
    /*
        Checks if an element exists in the LinkedList. Time Complexity: O(1) if list empty, O(n) where n is the # of elements in the list
     */
    func find(element: Int) -> Bool {
        
        if(self.isEmpty()) {
            print("LinkedList is Empty")
            return false
        } else {
            var currentNode = self.head
            while(currentNode?.next != nil) {
                if(currentNode?.data == element) {
                    return true
                }
                currentNode = currentNode?.next
            }
        }
        return false
    }
    
    /*
        Removes an element from the LinkedList. Time Complexity: O(1) if list empty or element is in the head, O(n) where n is the # of elements in the list
     */
    func remove(element: Int) -> Bool {
        
        if(self.isEmpty()){
            print("LinkedList is Empty")
            return false
        } else if (self.head?.data == element){
            self.head = self.head?.next
            self.size -= 1
            return true
            
        } else {
            var currentNode = self.head
            while(currentNode?.next != nil) {
                if(currentNode?.next?.data == element) {
                    let tempNode = currentNode?.next
                    currentNode?.next = tempNode?.next
                    self.size -= 1
                    return true
                }
                currentNode = currentNode?.next
            }
        }
        return false
    }
    
    /*
        Inserts an element at the given index of the LinkedList. Time Complexity: O(1) if list empty,
     */
    func insert(element: Int, at index: Int) {
        if(self.isEmpty()){
            print("LinkedList is Empty")
            return
        } else {
            let newNode = LinkedListNode(data: element)
            var currentNode = self.head
            var currentIndex = 0
            
            while(currentNode?.next != nil) {
                if(currentIndex + 1 == index) {
                    let tempNode = currentNode?.next
                    currentNode?.next = newNode
                    newNode.next = tempNode
                    self.size += 1
                }
                currentNode = currentNode?.next
                currentIndex += 1
            }
        }
    }
    
    /*
        Return the index of of an element in LinkedList. Time Complexity: O(1) if list empty, O(n) where n is the # of elements in the list
     */
    func index(element: Int) -> Int? {
        if(self.isEmpty()){
            print("LinkedList is Empty")
            return nil
        } else {
            var currentNode = self.head
            var currentIndex = 0
            while(currentNode != nil) {
                if(currentNode?.data == element) {
                    return currentIndex
                }
                currentNode = currentNode?.next
                currentIndex += 1
            }
        }
        return nil
    }
    
    func isEmpty() -> Bool {
        return self.size == 0
    }
}

var linkedList = LinkedList()
linkedList.append(data: 8)
linkedList.append(data: 10)
linkedList.append(data: 30)
linkedList.prepend(data: 7)
linkedList.append(data: 2)

linkedList.prepttyPrint()
print("Index of 30 is \(linkedList.index(element: 30))")
print("Index of 7 is \(linkedList.index(element: 7))")
print("Index of 2 is \(linkedList.index(element: 2))")



