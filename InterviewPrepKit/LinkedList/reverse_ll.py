def reverse_iterative(head):

    # create variable for prev as None, curr as root, next as None
    # traverse linked list
        # store the next node
        # change next node
        # change the next node to prev - REVERSING HAPPEN HERE
        # move previous and curr one step forward
    prev, next = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
