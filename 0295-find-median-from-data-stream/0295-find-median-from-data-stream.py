import heapq

class MedianFinder(object):

    def __init__(self):
        # max-heap (store negatives for Python's min-heap)
        self.small = []
        # min-heap
        self.large = []

    def addNum(self, num):
        # Step 1: Add to max-heap (small)
        heapq.heappush(self.small, -num)

        # Step 2: Balance by moving largest of small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 3: Ensure size property (small >= large)
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        # If odd, median is top of small
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If even, median is average of tops
        return (-self.small[0] + self.large[0]) / 2.0
