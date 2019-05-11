'''
    Question : Delete all the leaves from Binary Search Tree
    Time : 7 minutes
'''

from binarytree import BinarySearchTree

def delete_all_leaves(node):
    
    # Base Case - If not is None
    if not node:
        return 

    # Base Case - Check if node is leaf
    if (node.left is None) and (node.right is None):
        print("Leaf Deleted : ", node.data)
        node = None
        return

    if node.left:
        delete_all_leaves(node.left)

    if node.right:
        delete_all_leaves(node.right)

def main():
    
    tree = BinarySearchTree([1,2,3,4,5,6])
    delete_all_leaves(tree.root)

if __name__ == "__main__":
    main()