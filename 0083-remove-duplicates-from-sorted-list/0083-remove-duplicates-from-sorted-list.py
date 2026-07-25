# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head 
        seen = []
        prev = None
        while temp is not None:
            if temp.val not in seen:
                seen.append(temp.val)
                prev = temp
            else:
                prev.next = temp.next

            temp = temp.next
        return head