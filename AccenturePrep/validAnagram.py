def isAnagram(s: str, t: str) -> bool:
        """
        For a Anagram 2 strings must be spelled with same letters
        """
        # Checks if the strings are the same length
        if len(s) != len(t):
            return False
        
        # Makes a Hash Table for storing a count
        counter = {}
        
        # Gets a counter of each character
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        # Iterate the other string to see if we can detect a mismatch
        # Else decrement the counter by one 
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        
        # The strings are anagrams
        return True