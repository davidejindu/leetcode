class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, preq in prerequisites:
            graph[course].append(preq)

        visited, visiting = set(), set()

        def cycle(node):
            if node in visiting:
                return False

            if node in visited:
                return True

            visiting.add(node)

            for neighbor in graph[node]:
                if not cycle(neighbor):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True

        for course in range(numCourses):
            if not cycle(course):
                return False

        return True

        