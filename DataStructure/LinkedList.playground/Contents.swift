import UIKit
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

    func prepttyPrint() {

        if (self.isEmpty()) {
            print("LinkedList is Empty")
            return
        } else {
            var temp = self.head
            while(temp != nil){
                print("Data is \(temp?.data ?? 0)")
                temp = temp?.next
            }
        }
    }
    
    /*
        Adds an element at the end of the LinkedList
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
        Adds an element at the beginning of the LinkedList
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
        Checks if an element exists in the LinkedList
     */
    func found(element: Int) -> Bool {
        
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
    
    func remove() {
        
    }
    
    func search() {
        
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
linkedList.prepttyPrint()

print("Is 10 in the list: \(linkedList.found(element: 10))")
print("Is 3 in the list: \(linkedList.found(element: 3))")
print("Is 30 in the list: \(linkedList.found(element:30))")

