from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = 0
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
            
        return start
        
sol = Solution()
case1 = [1,3,5,6]

print(f"Input: nums = {case1}, target = {5} | Output: {sol.searchInsert(case1, 5)}")
print(f"Input: nums = {case1}, target = {2} | Output: {sol.searchInsert(case1, 2)}")
print(f"Input: nums = {case1}, target = {7} | Output: {sol.searchInsert(case1, 7)}")