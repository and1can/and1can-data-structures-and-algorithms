from collections import defaultdict
def dfs(graph, N): 
    visited = [0]*(N+1)
    curr = list(graph[1])
    while curr: 
        node = curr.pop(0)[0]
        if not visited[node]: 
            curr += list(graph[node])
            visited[node] = True
    visited = visited[1:]
    for node in visited: 
        if node: 
            continue
        else: 
            return False
    return True
        
    
class Solution:
    def minimumCost(self, N: int, conections: List[List[int]]) -> int:
        hashMap = defaultdict(list)
        for c in conections: 
            node_one = c[0]
            node_two = c[1]
            cost = c[2]
            hashMap[node_one].append((node_two, cost))
            hashMap[node_two].append((node_one, cost))
        if not dfs(hashMap, N):
            return -1 
        conections.sort(key = lambda x: x[2])
        # print(conections)
        parents = [i for i in range(N + 1)]
        # print(parents)
        def find(node, parent): 
            while node != parent: 
                node = parent
                parent = parents[node]
            return node
        cost = 0
        edge_count = 0
        for edge in conections: 
            node_one = edge[0]
            node_two = edge[1]
            curr_cost = edge[2]
            if find(node_one, parents[node_one]) != find(node_two, parents[node_two]):
                parents[find(node_two, parents[node_two])] = find(node_one, parents[node_one])
                cost += curr_cost
                edge_count += 1
                if edge_count == N + 1: 
                    return cost
            # print('node_one: ', node_one, 'node_two: ', node_two, 'parents: ', parents)
        # print('edge_count: ', edge_count)    
        return cost 