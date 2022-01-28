class Solution:
    def trim_space(self, s):
        s = list(s)
        l = len(s)
        left, right = 0, l - 1
        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1
        tmp = []
        while left <= right:
            if s[left] != " ":
                tmp.append(s[left])
            elif tmp[-1] != " ":
                tmp.append(s[left])
            left += 1
        # print(tmp)
        return tmp

    def reverse(self, x):
        l = len(x)
        left, right = 0, l - 1
        while left <= right:
            x[left], x[right] = x[right], x[left]
            left += 1
            right -= 1
        # print(x)
        return x

    def reverse_each(self, x):
        start = 0
        end = 0
        l = len(x)
        while start < l - 1:

            while end <= l - 1 and x[end] != " ":
                end += 1
            x[start: end] = self.reverse(x[start: end])
            start = end + 1
            end += 1
        print(x)
        return x

    def reverseWords(self, s: str) -> str:
        s = self.trim_space(s)
        s = self.reverse(s)
        s = self.reverse_each(s)
        return ''.join(s)
