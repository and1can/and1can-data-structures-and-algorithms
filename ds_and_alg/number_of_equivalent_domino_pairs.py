class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for sub_list in dominoes: 
            sub_list.sort()
        dom_map = {}
        dom_tuples = []
        for sub_list in dominoes: 
            dom_tuples.append((sub_list[0], sub_list[1]))
        dominoes = dom_tuples
        for sub_list in dominoes:  
            if sub_list not in dom_map: 
                dom_map[sub_list] = 1
            else: 
                dom_map[sub_list] += 1
        pairs = 0
        for key in dom_map.keys(): 
            curr = dom_map[key]
            pairs += (curr * (curr - 1) // 2)
        return pairs