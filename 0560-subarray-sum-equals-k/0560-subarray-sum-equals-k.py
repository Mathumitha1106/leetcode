class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        seen = {0: 1}  # prefix sum -> frequency

        for num in nums:
            prefix_sum += num
            # Check if there exists a prefix_sum - k
            if (prefix_sum - k) in seen:
                count += seen[prefix_sum - k]
            # Update frequency of prefix_sum
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return count
