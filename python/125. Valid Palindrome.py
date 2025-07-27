class Solution:
    def isPalindrome(self, s:str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
    
case1 = "A man, a plan, a canal: Panama"
case2 = "race a car"
case3 = " "

sol = Solution()

print(f"Input: {case1} | Output: {sol.isPalindrome(case1)}")
print(f"Input: {case2} | Output: {sol.isPalindrome(case2)}")
print(f"Input: {case3} | Output: {sol.isPalindrome(case3)}")
            