import Foundation


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
}

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
    
    func inorder(node: Node) -> [Int] {
        
        var visitedNodes = [Int]()
        
        // Visit the left subtree
        if(node.leftNode != nil) {
            self.inorder(node: node.leftNode ?? Node(data: 0))
        }
        
        // visit the root
        visitedNodes = visitedNodes + [node.data]
        
        // visit right subtree
        if(node.rightNode != nil) {
            self.inorder(node: node.rightNode ?? Node(data: 0))
        }
        
        return visitedNodes
    }
    
    
    func breadthFirstSearch() {
        
        let visitedNodes = ArrayQueue<Node>()
        visitedNodes.enqueue(element: rootNode ?? Node(data: 0))
        
        while (visitedNodes.size() > 0) {
            
            let currentNode = visitedNodes.dequeueu()
            if(currentNode.leftNode != nil) {
                visitedNodes.enqueue(element: currentNode.leftNode ?? Node(data: 0))
            } else if (currentNode.rightNode != nil) {
                visitedNodes.enqueue(element: currentNode.rightNode ?? Node(data: 0))
            }
        }
    }
}


