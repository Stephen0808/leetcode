class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        for i in s:
            tmp = i
            if tmp == '(':
                stack.append(')')
            elif tmp == '[':
                stack.append(']')
            elif tmp == '{':
                stack.append('}')
            elif not stack or stack[-1] != tmp:
                return False
            else:
                stack.pop()
        return True if not stack else False
