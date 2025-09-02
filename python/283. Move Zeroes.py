from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                
case1 = [0,1,0,3,12]
case2 = [1,0,4,13,42,0]

sol = Solution()

print(f"Input: {case1}")

sol.moveZeroes(case1)

print(f"Output: {case1}")

print("-" * 30)

print(f"Input: {case2}")

sol.moveZeroes(case2)

print(f"Output: {case2}")