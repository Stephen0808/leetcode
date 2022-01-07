# 滑动窗口
# Counter是一个哈希数组
def totalFruit(self, fruits: List[int]) -> int:
        count = Counter()
        res = 0
        i = 0
        for j, x in enumerate(fruits):
            count[x] += 1
            while len(count) >= 3:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            res = max(res, j-i+1)
        return res
