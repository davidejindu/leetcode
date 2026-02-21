class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """

        if cycle then its false else true

        [1,0]

        make a list of state of the node

        [UNVISTED, UNVISITED]

        when checking node change the state to visiting
        the check its neighbor 
        if its neighbor is visited return true if its visiting return false
        that means we went back to the node without returning making it a
        cycle


        """
        
        courses = defaultdict(list)

        for a,b in prerequisites:
            courses[b].append(a)

        states = ["UNVISITED"] * numCourses

        
        def dfs(node):

            state = states[node]

            if state == "VISITING": return False

            elif state == "VISITED": return True

            states[node] = "VISITING"

            for neighbor in courses[node]:
                if not dfs(neighbor):
                    return False

            states[node] = "VISITED"
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


