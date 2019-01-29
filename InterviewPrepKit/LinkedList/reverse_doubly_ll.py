def reverse(head):

    #edge cases
    if head is None:
        return head

    if head.next is None:
        return head

    curr = head
    temp = None
    while curr is not None:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
        
    return temp.prev
