
class Solution:
    def reverseString(self, s: list[str]) -> None:
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Example usage
s = ["h", "e", "l", "l", "o"]
solution = Solution()
solution.reverseString(s)
print(s)  # Output: ["o", "l", "l", "e", "h"]
