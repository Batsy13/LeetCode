class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0 and ((n) & (n-1) == 0):
            return True
        else:
            return False
        
case1 = 1
case2 = 16
case3 = 3
case4 = 256

sol = Solution()

print(f"Input {case1} | Output: {sol.isPowerOfTwo(case1)}")
print(f"Input {case2} | Output: {sol.isPowerOfTwo(case2)}")
print(f"Input {case3} | Output: {sol.isPowerOfTwo(case3)}")
print(f"Input {case4} | Output: {sol.isPowerOfTwo(case4)}")