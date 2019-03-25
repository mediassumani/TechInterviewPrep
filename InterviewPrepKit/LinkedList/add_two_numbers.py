class Solution(object):
    def reverse(self, ll):

        prev = None
        next_elem = None
        curr = ll

        while curr:
            next_elem = curr.next
            curr.next = prev
            prev = curr
            curr = next_elem
        return prev



    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverse(l1)
        saver = 0
        head = None
        # traverse through both list
        while l1 and l2:
            temp_sum = l1.val + l2.val
            if saver != 0:
                temp_sum += saver
            if temp_sum >= 10:
                saver = 1
                temp_sum = 0

            temp_node = ListNode(temp_sum)
            if head is not None:
                head = temp_node
                head.next = l1
            else:
                head = temp_node
                head.next = l1
            l1 = l1.next
            l2 = l2.next

        print(head.val)


        #return self.reverse(head)
