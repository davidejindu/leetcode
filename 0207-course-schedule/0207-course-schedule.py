class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courseMap = defaultdict(list)

        for preq, course in prerequisites:
            courseMap[course].append(preq)

        visiting, visited = set(), set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            for preq in courseMap[course]:
                if not dfs(preq):
                    return False

            visiting.remove(course)
            visited.add(course)
            return True

        for preq in range(numCourses):
            if not dfs(preq):
                return False

        return True