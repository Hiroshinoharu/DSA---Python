class Solution:
    def longestPalindrome(self, s:str) -> str:
        result = ""
        
        for i in range(len(s)):
            # Odd length palindrome
            pal = self.check_palindrome(s, i, i)
            if len(pal) > len(result):
                result = pal

            # Even length palindrome
            pal = self.check_palindrome(s, i, i + 1)
            if len(pal) > len(result):
                result = pal

        return result

    def check_palindrome(self,s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

# Example usage
s = "rotatorvibratorpeepwow"
solution = Solution()
print(solution.longestPalindrome(s))  # Output: "rotator"