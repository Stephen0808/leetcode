class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # print(head)
        if not head:
            return
        # 这里设置ppre=None是很有学问的
        ppre = None
        pre = head
        while pre:
            # cur先保存pre的后一个量
            cur = pre.next
            # 先把第一个进行反转
            pre.next = ppre
            # 让ppre进行step，至pre
            ppre = pre
            # 让pre step
            pre = cur
        return ppre
