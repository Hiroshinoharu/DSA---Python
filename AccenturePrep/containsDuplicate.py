class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Set a set to keep record of entries until a duplicate is found
        store = set()

        # Iterate through the array
        for num in nums:
            # If the number was in the set
            if num in store:
                # Duplicate is found
                return True
            # Else add it to the hashset
            store.add(num)
        # No duplicates found
        return False