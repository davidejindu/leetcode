class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle, visited = set(), set()
        output = []

        courseMap = defaultdict(list)

        for course, preq in prerequisites:
            courseMap[course].append(preq)

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True

            cycle.add(course)

            for preq in courseMap[course]:
                if not dfs(preq):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            output.append(course)

            return True


        for course in range(numCourses):
            if not dfs(course):
                return []

        return output