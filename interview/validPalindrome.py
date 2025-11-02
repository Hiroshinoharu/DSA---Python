def isPalindrome(s: str) -> bool:
    # Normalise the string 
    filtered = [c.lower() for c in s if c.isalnum()]
    
    # Adopt a 2-pointer Approach
    left = 0
    right = len(filtered) - 1

    # Iterate through the pointers
    while left < right:
        # If the charactewr on the right isn't like the left
        if filtered[left] != filtered[right]:
            # Its invlaid palindrome
            return False
        else:
            # Otherwise increase the left and decrease the right
            left += 1
            right -= 1
    # If the loop didn't terminates its a valid Plaindrome.
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))