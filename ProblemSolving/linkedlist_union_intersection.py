"""
Given two Linked Lists, create union and intersection lists
that contain union and intersection of the elements present
in the given lists. Order of elments in output lists doesn’t matter.
"""
from linkedlist import LinkedList

def union_and_intersection(ll_one, ll_two):
    """ Return the a tuple that contains a union and intersection ll of the two lists"""

    union_ll = LinkedList()
    intersection_ll = LinkedList()

    # Edge Cases
    if ll_one.length() is 0 and ll_two.length() is 0:
        raise ValueError("Both List are empty.")
    if ll_one.length() is 0:
        return (union_ll, ll_two)
    elif ll_two.length() is 0:
        return (union_ll, ll_one)

    outer_current_node = ll_one.head # the current node(s) of the first list argument

    # Traverse both lists
    while outer_current_node is not None:
        inner_current_node = ll_two.head # the current node(s) of the second list argument
        while inner_current_node is not None:
            # checks if element are equal, forming union ll
            if inner_current_node.data == outer_current_node.data :
                union_ll.append(outer_current_node.data)

                # checks if all elemnt from ll_two is appended, avoiding duplicates
            if intersection_ll.length() <= ll_two.length():
                intersection_ll.append(inner_current_node.data)
            inner_current_node = inner_current_node.next

        intersection_ll.append(outer_current_node.data)
        outer_current_node = outer_current_node.next

    return (union_ll, intersection_ll)

def main():

    list_one = LinkedList()
    list_two = LinkedList()

    list_one.append(1)
    list_one.append(4)
    list_one.append(7)

    list_two.append(3)
    list_two.append(5)
    list_two.append(7)

    print(union(list_one, list_two))

if __name__ == '__main__':
    main()
