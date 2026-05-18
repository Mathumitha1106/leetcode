from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        need = Counter(t)   # frequency of chars in t
        missing = len(t)    # total chars still needed
        left = start = end = 0

        for right, char in enumerate(s, 1):  # right is 1-based
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            # When all chars are covered
            if missing == 0:
                # Move left to shrink window
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                # Update best window
                if end == 0 or right - left < end - start:
                    start, end = left, right
                # Prepare for next window
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]
