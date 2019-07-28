from collections import defaultdict
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        edges = defaultdict(list)
        semester = 0
        indegree = defaultdict(lambda: 0)
        for rel in relations: 
            edges[rel[0]].append(rel[1])
            indegree[rel[1]] += 1
        sources = []
        for i in range(1, N + 1): 
            if indegree[i] == 0: 
                sources.append(i)
        visited = [0]*(N + 1)
        while (sources): 
            # print('sources: ', sources, 'indegree: ', indegree)
            nextSource = []
            for source in sources: 
                if not visited[source]: 
                    for neighbor in edges[source]: 
                        indegree[neighbor] -= 1
                        if not visited[neighbor] and indegree[neighbor] == 0: 
                            nextSource.append(neighbor)
                del indegree[source]
            sources = nextSource
            visited[source] = True
            semester += 1
        if len(indegree.keys()) != 0: 
            return -1
        return semester