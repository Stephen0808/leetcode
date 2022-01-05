def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftboard(nums, target):
            if not nums:
                return -1
            l, r = 0, len(nums) - 1
            while(l <= r):
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return l
        
        lb = leftboard(nums, target)  # 若不存在，即为插入位置
        rb = leftboard(nums, target+1) - 1  # 若存在，即为+1值的最左侧
        print(lb, rb)
        if rb >= lb:
            return [lb, rb]
        else:
            return [-1, -1]
