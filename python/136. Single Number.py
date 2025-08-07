from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        counts = {}
        
        for num in nums:
            if num not in nums:
                counts[num] = 1
            else:
                counts[num] += 1
                
                
        for num, count in counts.items():
            if count == 1:
                return num