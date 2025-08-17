from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)

        count = 0
        res = 0

        for i in range(size):
            if(count == 0):
                res = nums[i]

            if res == nums[i]:
                count += 1
            else:
                count -= 1
            
        return res