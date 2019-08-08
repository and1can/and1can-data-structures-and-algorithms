from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_map = defaultdict(lambda: 0)
        for i in arr2: 
            count_map[i] = 0
        print(count_map)
        rest = []
        for j in arr1: 
            if j in count_map: 
                count_map[j] += 1
            else: 
                rest.append(j)
        final_array = []
        for key in arr2: 
            for j in range(count_map[key]):
                final_array.append(key)
        
        rest.sort()
        final_array += rest
        return final_array