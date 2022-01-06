def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums) - 1 
        i, j, k = 0, n, n
        ans = [0] * (n + 1)
        while(i <= j):
            if nums[i] ** 2 > nums[j] ** 2:
                ans[k] = nums[i] ** 2
                i += 1
            else:
                ans[k] = nums[j] ** 2
                j -= 1
            k -= 1
        return ans
