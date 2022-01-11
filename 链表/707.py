class Node:
    def __init__(self, val):
        self.next = None
        self.val = val
        
class MyLinkedList:

    def __init__(self):
        self._head = Node(0)
        self._count = 0

    def get(self, index: int) -> int:
        pre = self._head
        if 0 <= index < self._count:
            for _ in range(index+1):
                pre = pre.next
            return pre.val
        else:
            return -1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self._count:
            return
        
        self._count += 1
        pre = Node(0)
        cur = self._head
        
        # 指针悬空没有问题，但是有指向就会出现环
        # pre.next = cur
        # 如果不悬空，那么就要同时交换值
        # pre, cur = cur, cur.next
        
        for _ in range(index+1):
            pre = cur
            cur = cur.next
        add_node = Node(val)
        add_node.next = cur
        pre.next = add_node

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self._count, val)

    def deleteAtIndex(self, index: int) -> None:
        pre = Node(0)
        pre.next = self._head
        cur = self._head
        if 0 <= index < self._count:
            for _ in range(index+1):
                pre = cur
                cur = cur.next
            pre.next = cur.next
            self._count -= 1
        else:
            return
