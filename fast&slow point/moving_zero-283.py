
# 本题应该将情况分为指向0和指向非0的情况
# 共同指向非0时同样进行值交换，没有任何影响
# fast超前的格数内全为0
def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast, slow = 0, 0
        while(fast < len(nums)):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
        return slow
