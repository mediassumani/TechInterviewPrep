
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):

                head = ListNode(0)
        carry = 0
        a, b, current = l1,l2, head

        while l1 is not None or l2 is not None:

            x = a.val if a != None else 0
            y = b.val if b != None else 0
            sum = x+y+carry
            carry = sum/10
            current.next = ListNode(sum%10)
            current = current.next
            if a != None:
                a = a.next
            if b != None:
                b = b.next

        if carry > 0:
            current.next = ListNode(carry)

        return head.next
