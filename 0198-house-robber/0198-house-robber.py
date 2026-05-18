class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # dp[i] = max money up to house i
        prev1, prev2 = 0, 0  # prev1 = dp[i-1], prev2 = dp[i-2]

        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)  # rob current or skip
            prev2 = temp

        return prev1

        