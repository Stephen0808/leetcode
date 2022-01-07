
# 解法一：
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        fast, slow = 0, 0
        s = 0
        ans = float("inf")
        while(fast <= len(nums)):
            if s >= target:
                s -= nums[slow]
                ans = min(ans, fast - slow)
                slow += 1
            else:
                # 可能会出现fast超界但是数组和仍大于target的情况，此时需要给予裕度，等到下一次小于target的时候再结束循环
                if fast != len(nums):
                    s += nums[fast]
                fast += 1

        return ans if ans != float("inf") else 0
     
# 解法二：
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        index = 0
        s = 0
        ans = float("inf")
        for i in range(len(nums)):
            s += nums[i]
            while(s >= target):
                ans = min(ans, i-index+1)
                s -= nums[index]
                index += 1

        return ans if ans != float("inf") else 0
