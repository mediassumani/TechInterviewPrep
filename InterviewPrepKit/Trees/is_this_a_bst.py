def checkBST(root):

    seen_elements = []
    if root is None:
        return False

    else:
        curr_node = root
        if curr_node.data not in seen_elements:
            seen_elements.append(curr_node.data)
        else:
            return False

        if curr_node.left:
            if curr_node.left.data < curr_node.data:
                checkBST(curr_node.left)
            else:
                return False

        if curr_node.right:
            if curr_node.right.data > curr_node.data:
                checkBST(curr_node.right)
            else:
                return False

    return True
