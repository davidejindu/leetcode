"""

total # of courses labeled from 0 to # of courses

given an array [0,1] where i need to take 0 if i want to take 1

input: how many courses, array mapping courses i need to take 

output: if i can take all the courses

the only way i wouldnt be able to finish a course if there is a cycle

so i need to create an adjancy list
do a dfs where i add the node to a visit list and then check its neighbors
if the neighbor is in visited list it means ive looped so i return False

i keep going till i reach end and keep returning true at the end

[1:0]

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        visiting,visited = set(), set()


        #make an adjancy list the course is key and preq is value
        for course, preq in prerequisites:
            courseMap[course].append(preq)


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

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True