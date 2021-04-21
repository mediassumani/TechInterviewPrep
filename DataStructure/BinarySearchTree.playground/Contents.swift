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
}
