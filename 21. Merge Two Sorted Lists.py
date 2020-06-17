# Definition for singly-linked list.
from graphviz import Digraph
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.val)

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
                if l1.val > l2.val:
                    l1, l2 = l2, l1
                l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2



    def visualize_ListNode(self, head):
        dot = Digraph()
        dot.attr(rankdir='LR')
        while head:
            dot.node(str(head), label=str(head.val))
            if head.next is not None:
                dot.edge(str(head), str(head.next))
            head = head.next
        return dot

def execute() -> object:
    l1 = ListNode([1, 2, 4])
    l2 = ListNode([1, 3, 4])
    sol = Solution()
    print(sol.mergeTwoLists(l1, l2))

if __name__ == "__main__":
    execute()
