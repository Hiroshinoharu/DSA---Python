class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Base cases
        if len(needle) > len(haystack):
            return -1
        elif len(needle) == 0:
            return 0

        # Iterate through haystack
        for i in range(len(haystack)):
            # Slice haystack from i to i + len(needle)
            if haystack[i : i + len(needle)] == needle:
                return i
        
        return -1