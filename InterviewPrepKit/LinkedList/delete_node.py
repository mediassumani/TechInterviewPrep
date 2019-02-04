def removeNthFromEnd(self, head, n):
    
    if head.next is None:
        return []

    length = 0
    curr = head
    target_node = None
    counter = 0


    # get the length of the LL
    while curr:
        length += 1
        curr = curr.next

    pivot_point = length - n
    curr = head

    if length == 2 and pivot_point == 1:
        curr.next = None
        return head

    if length == 2 and pivot_point == 0:
        curr.val, curr.next.val = curr.next.val, curr.val
        curr.next = None
        return head

    while curr:
        # if curr.next.next is None:
        #     curr.next = None
        #     return head
        if counter == pivot_point:
            target_node = curr
            if target_node.next is None:
                target_node = None
                return head


            target_node.val, target_node.next.val = target_node.next.val, target_node.val
            target_node.next = target_node.next.next
            return head
        counter += 1
        curr = curr.next
