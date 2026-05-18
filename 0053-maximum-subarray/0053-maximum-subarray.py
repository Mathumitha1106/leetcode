class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize with the first element
        current_sum = max_sum = nums[0]

        # Iterate through the rest
        for num in nums[1:]:
            # Either extend the current subarray or start new
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

        