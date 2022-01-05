# 第一种解法
# 左闭右开 & 左开右闭
def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if not nums:
            return -1
        while(True):
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if target < nums[m] and target >= nums[l]:
                r = m - 1
            elif target <= nums[r] and target > nums[m]:
                l = m + 1
            else:
                return -1

# 第二种解法
# 左闭右闭
def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if not nums:
            return -1
        while(l <= r):
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1
      
# 第三种解法
# 左闭右开
def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)  # r的值要大于右边界一个单位
        if not nums:
            return -1
        while(l < r):
            m = (l + r) // 2
            if nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
