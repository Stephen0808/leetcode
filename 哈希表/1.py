class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = {}
        # 每进一个元素就会判断一次
        for idx, val in enumerate(nums):
            if target - val in record:
                return [record[target - val], idx]
            else:
                record[val] = idx
