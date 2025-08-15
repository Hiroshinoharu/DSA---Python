from typing import List

class Solution:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    You can solve this problem using a hash map to store the indices of the numbers.
    
    Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    
    Example:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    
    Example:
    Input: nums = [3,3], target = 6
    Output: [0,1]
    
    Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.
    - The order of the output does not matter.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in store:
                return [store[complement], i]
            else:
                store[nums[i]] = i
        return []

# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]