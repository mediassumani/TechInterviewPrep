from binarytree import BinarySearchTree

'''
    Question : Delete a binary tree by deallocating all its nodes.
    Time : 10 minutes
    Solution : Depth first Search (Post Order)
'''
def visit(node):

    print("Node deallocated = ", node)
    node = None
    return 

def delete_bt(node):
    
    curr = node

    if curr.left:
        delete_bt(curr.left)

    if curr.right:
        delete_bt(curr.right)

    visit(curr)

def main():
    
    tree = BinarySearchTree(['B', 'A', 'C'])
    delete_bt(tree.root)


if __name__ == "__main__":
    main()