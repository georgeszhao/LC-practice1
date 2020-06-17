class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data atribute"""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data parameter"""
        self.data = new_data

    def get_next(self):
        """"Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """"Return the existing value of the self.next attribute with new_next parameter"""
        self.next = new_next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        k %= n
        if k == 0:
            return head
        old_tail.next = head
        new_tail = head
        for i in range(n-k-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head

def execute():
    head = [1, 2, 3, 2, 1]
    k = 1
    sol = Solution()
    print(sol.rotateRight(head, k))


if __name__ == "__main__":
    execute()


