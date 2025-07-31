from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        
        for i in range(size - 1, -1, -1):
            
            if digits[i] + 1 != 10:
                
                digits[i] += 1
                
                return digits
        
            digits[i] = 0
            
            if i == 0:
                return [1] + digits
            
            return digits
        
sol = Solution()

case1 = [1,2,3]
case2 = [4,3,2,1]
case3 = [9]

print(f"Input: {case1} | Output: {sol.plusOne(case1)}")
print(f"Input: {case2} | Output: {sol.plusOne(case2)}")
print(f"Input: {case3} | Output: {sol.plusOne(case3)}")