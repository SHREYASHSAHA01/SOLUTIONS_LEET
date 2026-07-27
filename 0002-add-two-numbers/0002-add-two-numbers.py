# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        head = l3
        temp1 =l1
        temp2 = l2
        carry = 0
        while temp1 or temp2 or carry:
            total = (temp1.val if temp1 else 0) + (temp2.val if temp2 else 0 )+ carry
            l3.next = ListNode(total%10)
            carry = total//10
            l3 = l3.next
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
        return head.next
        