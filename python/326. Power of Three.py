class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n //= 3
        
        return n == 1
    
case1 = 3
case2 = 27
case3 = 612315

sol = Solution()

print(f"Input: {case1} | Output: {sol.isPowerOfThree(case1)}")
print(f"Input: {case2} | Output: {sol.isPowerOfThree(case2)}")
print(f"Input: {case3} | Output: {sol.isPowerOfThree(case3)}")