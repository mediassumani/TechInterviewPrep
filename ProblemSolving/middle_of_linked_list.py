'''
Given a singly linked list, find middle of the linked list. For example,
if given linked list is 1->2->3->4->5 then output should be 3.
If there are even nodes, then there would be two middle nodes,
we need to print second middle element. For example, if given
linked list is 1->2->3->4->5->6 then output should be 4.
'''
from linkedlist import LinkedList


def find_middle(linked_list):

    counter = 0
    length = linked_list.length()
    current_node = linked_list.head

    while current_node is not None:
        counter += 1
        if counter <= length /2:
            current_node = current_node.next
        else:
            if length % 2 == 0:
                return current_node.next.data
            else:
                return current_node.data

def main():

    list_one = LinkedList()
    list_two = LinkedList()

    list_one.append(1)
    list_one.append(2)
    list_one.append(3)

    list_two.append(1)
    list_two.append(2)
    list_two.append(3)
    list_two.append(4)

    print(find_middle(list_one))
    print(find_middle(list_two))

if __name__ == "__main__":
    main()
