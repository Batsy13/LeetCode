class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        original = x
        
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
            
        return reverse == original
    
case1 = 121
case2 = -121
case3 = 10

sol = Solution()

print(f"Input: {case1} | Output: {sol.isPalindrome(case1)}")
print(f"Input: {case2} | Output: {sol.isPalindrome(case2)}")
print(f"Input: {case3} | Output: {sol.isPalindrome(case3)}")