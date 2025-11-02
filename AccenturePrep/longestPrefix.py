class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # We intialise a empty result
        res = ""

        # We iterate through the whole string of the first element
        for i in range(len(strs[0])):
            # Iterate through the array
            for s in strs:
                # If the index is the same size as string or the character 
                # of the string doesn't match the character of the first string in the array
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # Else add the character to the overall result
            res += strs[0][i]
        # Return the result
        return res