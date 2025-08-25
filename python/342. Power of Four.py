class Solution: 
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 4 == 0:
            n //= 4
            
        return n == 1
    
case1 = 16
case2 = 5
case3 = 1

sol = Solution()

print(f"Input: {case1} | Output: {sol.isPowerOfFour(case1)}")
print(f"Input: {case2} | Output: {sol.isPowerOfFour(case2)}")
print(f"Input: {case3} | Output: {sol.isPowerOfFour(case3)}")