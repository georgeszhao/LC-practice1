# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        while head and head.next:
            first_node, second_node = head, head.next
            first_node.next = second_node.next
            second_node.next = first_node
            prev_node.next = second_node
            prev_node = first_node
            head = first_node.next
        return dummy.next