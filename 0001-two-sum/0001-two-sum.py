class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store number -> index
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                # Found the pair
                return [seen[complement], i]
            # Store the current number with its index
            seen[num] = i
