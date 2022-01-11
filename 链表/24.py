class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(0, head)
        res = pre
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next
        return res.next
