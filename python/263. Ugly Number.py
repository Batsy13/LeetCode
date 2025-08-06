class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        
        return n == 1

case1 = 6
case2 = 1
case3 = 14

sol = Solution()

print(f"Input: {case1} | Output: {sol.isUgly(case1)}")
print(f"Input: {case2} | Output: {sol.isUgly(case2)}")
print(f"Input: {case3} | Output: {sol.isUgly(case3)}")