import Foundation

/*
    A Queue is an ordered collection where adding a new element happens in the back(enqueue)
    and removing an existing element happens in the front(dequeueu)
 
    * A Queue follows the FIFO  principle = first in -> first out
    * A Queue can be implemented using an Array(or a LinkedList as well) or a Node.
 */
class ArrayQueue <T> {
    
    private var items = [T]()
    
    func enqueue(element: T) {
        self.items.append(element)
    }
    
    func dequeueu() -> T {
        
        let element = self.items.removeFirst()
        return element
    }
    
    func isEmpty() -> Bool {
        return self.size() == 0
    }
    
    func size() -> Int {
        return self.items.count
    }
    
    func prettyPrint() {
        
        for (index, value) in self.items.enumerated() {
            print("Position \(index) is \(value)")
        }
    }
}


let arrayQueue = ArrayQueue<String>()
arrayQueue.enqueue(element: "Medi")
arrayQueue.enqueue(element: "Medo")
arrayQueue.enqueue(element: "Meda")
arrayQueue.prettyPrint()


arrayQueue.dequeueu()
arrayQueue.prettyPrint()
arrayQueue.enqueue(element: "Mede")
arrayQueue.prettyPrint()
