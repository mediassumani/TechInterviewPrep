import Foundation

/*
    A Stack is an ordered collection of items where addition of new items and removal of existings
    items happens only from the top.
 
    * A Stack data structure follows a LIFO principle - last in -> first out.
    * A Stack data structure can be built with an array or Node.
 */

class ArrayStack <T> {
    
    private var items: [T]
    
    init() {
        self.items = [T]()
    }
    
    // Add an element at the top of the Stack
    func push(element: T) {
        self.items.append(element)
    }
    
    
    // Remove and return the top of the Stack. Time Complexity: O(n) where n is the # of elements in the stack
    func pop() -> T {
        let element = self.items.remove(at: self.size() - 1)
        return element
    }
    
    // Return the top of the stack. Time Complexity: O(1)
    func peak() -> T {
        return self.items[self.size() - 1]
    }
    
    
    // Return the size of the Stack. Time Complexity: O(1)
    func size() -> Int {
        return self.items.count
    }
    
    // Returns wheter or not the stack is empty. Time Complexity: O(1)
    func isEmpty() -> Bool{
        return self.size() == 0
    }
    
    func prettyPrint() {
    
        var index = self.size() - 1
        while (index >= 0) {
            print("Element: \(self.items[index])")
            index -= 1
        }
    }
}


let stack = ArrayStack<String>()
stack.push(element: "Betterment")
stack.push(element: "Wealthfront")
stack.push(element: "Wealthsimple")

stack.prettyPrint()

stack.pop()
stack.prettyPrint()
print("Peark is \(stack.peak())")


