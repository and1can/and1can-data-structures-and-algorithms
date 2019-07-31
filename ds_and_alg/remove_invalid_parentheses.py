class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.results = set([])
        self.min = len(s)
        self.helper(list(s), '', 0, 0, len(s) // 2, 0)
        return self.results
    
    def helper(self, string, curr_pattern, open_count, close_count, half_length, remove_count):  
        if open_count < close_count: 
            return 
        if open_count > half_length: 
            return 
        if len(string) == 0: 
            if open_count == close_count and remove_count <= self.min: 
                if remove_count < self.min: 
                    self.results = set([curr_pattern])
                    self.min = remove_count
                else: 
                    if curr_pattern not in self.results: 
                        self.results.add(curr_pattern)
                return
            else: 
                return
        if string[0] == '(': 
            new_list = list(curr_pattern)
            new_list.append('(')
            self.helper(string[1:], ''.join(new_list), open_count + 1, close_count, half_length, remove_count)
            self.helper(string[1:], curr_pattern, open_count, close_count, half_length, remove_count + 1)
        elif string[0] == ')': 
            new_list = list(curr_pattern)
            new_list.append(')')
            self.helper(string[1:], ''.join(new_list), open_count, close_count + 1, half_length, remove_count)
            self.helper(string[1:], curr_pattern, open_count, close_count, half_length, remove_count + 1)
        else: 
            new_list = list(curr_pattern)
            new_list.append(string[0])
            self.helper(string[1:], ''.join(new_list), open_count, close_count, half_length, remove_count)