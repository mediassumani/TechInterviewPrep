def has_cycle(head):


     # Check edge case
     if head.next is None:
         return False

     curr_node = head
     prev_node = None
     next_node = None

     while curr_node is not None:
         if next_node is not curr_node:
             prev_node = curr_node
             curr_node = curr_node.next
             next_node = curr_node.next
         else:
             return True

    return False
