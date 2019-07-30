from collections import defaultdict

class Solution:
    def minimumCost(self, N: int, conections: List[List[int]]) -> int:
        conections.sort(key = lambda x: x[2])
        parents = [i for i in range(N + 1)]
        def find(node): 
            parent = parents[node]
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
            if find(node_one) != find(node_two):
                parents[find(node_two)] = find(node_one)
                cost += curr_cost
                edge_count += 1
                if edge_count == N + 1: 
                    return cost
        return -1 if edge_count < N - 1 else cost 