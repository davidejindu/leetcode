class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for source, destinations in sorted(tickets, reverse=True):
            graph[source].append(destinations)

        stack = ["JFK"]
        result = []

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())

            result.append(stack.pop())

        return result[::-1]