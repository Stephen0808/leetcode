class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = {}
        count = 0
        for x in nums1:
            for y in nums2:
                if x + y not in hashmap:
                    hashmap[x + y] = 1
                else:
                    hashmap[x + y] += 1
        for m in nums3:
            for n in nums4:
                if 0 - n - m in hashmap:
                    count += hashmap[0 - n - m]
        return count
