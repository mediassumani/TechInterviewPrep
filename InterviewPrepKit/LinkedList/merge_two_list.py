# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        solution from Ali
        """

        # edge cases
        if not l1:
            return l2
        if not l2:
            return l1


        if l1.val <= l2.val:
            new_head = l1
            new_list = l1
            l1 = l1.next
        else:
            new_head = l2
            new_list = l2
            l2 = l2.next

        while l1 and l2:
            if l1.val <= l2.val:
                new_list.next = l1
                new_list = l1
                l1 = l1.next
            else:
                new_list.next = l2
                new_list = l2
                l2 = l2.next
        if l1:
            new_list.next = l1
        if l2:
            new_list.next = l2
        return new_head
