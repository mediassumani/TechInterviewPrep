'''
Given a singly linked list, delete middle of the linked list.For example,
if given linked list is 1->2->3->4->5 then output should be 3.
If there are even nodes, then there would be two middle nodes,
we need to print second middle element. For example, if given
linked list is 1->2->3->4->5->6 then output should be 4.
'''

from linkedlist import LinkedList
from middle_of_linked_list import find_middle

def delete_middle(linked_list):
    """ Delete the middle of a linked list"""

    if linked_list.head is None:
        return linked_list

    if linked_list.length() == 1:
        linked_list.head = None
        return linked_list.head

    middle_element = find_middle(linked_list)
    linked_list.delete(middle_element)
    return linked_list

def main():
        list_one = LinkedList()
        list_two = LinkedList()
        list_three = LinkedList()
        list_four = LinkedList()


        list_one.append(1)
        list_one.append(2)
        list_one.append(3)

        list_two.append(1)
        list_two.append(2)
        list_two.append(3)
        list_two.append(4)

        list_four.append(7)

        print(delete_middle(list_one))
        print(delete_middle(list_two))
        print(delete_middle(list_three))
        print(delete_middle(list_four))



if __name__ == "__main__":
    main()
