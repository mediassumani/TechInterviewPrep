import Foundation

/*
    A Queue is an ordered collection where adding a new element happens in the back(enqueue)
    and removing an existing element happens in the front(dequeueu)
 
    * A Queue follows the FIFO  principle = first in -> first out
    * A Queue can be implemented using an Array(or a LinkedList as well) or a Node.
 */

class Node<T> {
    
}

class NodeQueue <T> {
    
}
class ArrayQueue <T> {
    
    private var items = [T]()
    
    func enqueue(element: T) {
        self.items.append(element)
    }
    
    func dequeueu() {
        
    }
    
    func isEmpty() -> Bool {
        return false
    }
    
    func size() -> Int {
        return 1
    }
}
