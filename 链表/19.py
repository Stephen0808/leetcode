# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = 0, 0
        
        # 排除只有一个值的情况
        if head.next == None:
            return 
        fast = head
        slow = head
        count = 0
        
        # 建立头节点
        pre_head = ListNode()
        pre = pre_head
        pre_head.next = head
        
        # fast和slow间保持n距离
        while fast.next != None:
            fast = fast.next
            count += 1
            if count >= n:
                pre = slow
                slow = slow.next
        print(slow)
        # if slow == head:
        #     return slow.next
        # 删除某结点
        pre.next = pre.next.next
        return pre_head.next
        
