class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}   # character -> last index
        left = 0    # left boundary of window
        max_len = 0

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                # Move left boundary past the duplicate
                left = seen[char] + 1
            seen[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
