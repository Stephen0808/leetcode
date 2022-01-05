def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 0, x
        while(l <= r):
            m = (l + r) // 2
            if m ** 2 > x:  # 注意：仅当==的值不重要时才用大于等于符号
                r = m - 1
            elif m ** 2 < x:
                l = m + 1
            else:
                return m
        return r  # 输出的都是最先更新的值
