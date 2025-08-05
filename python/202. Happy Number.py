class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = self.sumSquares(n)
            
            if n == 1:
                return True
        
        return False
    
    def sumSquares(self, n: int) -> int:
        total = 0
        
        while n:
            digit = n % 10
            digit = digit ** 2
            total += digit
            n = n // 10
        return total
    
case1 = 19
case2 = 2

sol = Solution()

print(f"Input: {case1} | Output: {sol.isHappy(case1)}")
print(f"Input: {case2} | Output: {sol.isHappy(case2)}")