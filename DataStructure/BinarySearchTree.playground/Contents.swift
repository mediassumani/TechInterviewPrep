import Foundation


class Node {
    
    var data: Int
    var leftNode: Node?
    var rightNode: Node?
    
    init(data: Int) {
        self.data = data
        self.leftNode = nil
        self.rightNode = nil
    }
    
    func isLeaf() -> Bool {
        return false
    }
    
    func isBranch() -> Bool {
        return false
    }
    
    func height() -> Int {
        return 0
    }
}

class BinarySearchTree {
    
    var rootNode: Node?
    init() {
        self.rootNode = nil
    }
    
    func size() {
        
    }
    
    func isEmpty() {
        
    }
    
    /**
     return a boolean indicating whether item is present in the tree
     */
    func contains(value: Int) {
        
    }
    
    /**
     return an item in the tree matching the given item, or None if not found
     */
    func search(item: Int) {
        
    }
    
    /*
     insert the given item in order into the tree
     */
    func insert(itetm: Int) {
        
    }
    
}
