class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

        def dfs(course):
            if visited[course] == 1:  # cycle detected
                return False
            if visited[course] == 2:  # already checked
                return True

            visited[course] = 1  # mark as visiting
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 2  # mark as visited
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
