# LeetCode 269. Alien Dictionary 
# Submission accepted 
class Node(object): 
        def __init__(self, value): 
            self.val = value
            self.next = []
        
        def __repr__(self): 
            return 'val: ' + str(self.val) +  ' next: ' + str(self.next.val) if self.next else str(self.next)
            
def buildGraph(currWord, nextWord, nodes, sources, indegrees): 
        n = max(len(currWord), len(nextWord))
        foundDiff = False
        for i in range(n):
            currChar = None
            nextChar = None
            if i < len(currWord):
                currChar = currWord[i]
                if currChar not in nodes: 
                    nodes[currChar] = Node(currChar)
                    sources[currChar] = 0
                    indegrees[currChar] = 0
            if i < len(nextWord):
                nextChar = nextWord[i]
                if nextChar not in nodes: 
                    nodes[nextChar] = Node(nextChar)
                    sources[nextChar] = 0
                    indegrees[nextChar] = 0
            if currChar != nextChar and not foundDiff and nextChar and currChar: 
                foundDiff = True
                nodes[currChar].next.append(nodes[nextChar])
                indegrees[nextChar] += 1
                if nextChar in sources: 
                    del sources[nextChar]
        return nodes
    
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) <= 1: 
            return words[0]
        nodes = {}
        sources = {}
        indegrees = {}
        for i in range(len(words) - 1): 
            currWord = words[i]
            nextWord = words[i + 1]
            buildGraph(currWord, nextWord, nodes, sources, indegrees)
        outputList = []
        outputHash = {}
        sourceQueue = list(sources.keys())
        while (sourceQueue): 
            curr = str(sourceQueue.pop(0))
            outputList.append(curr)
            currNode = nodes[curr]
            if currNode.next:
                for nextNode in currNode.next:
                    indegrees[nextNode.val] -= 1
                    if not indegrees[nextNode.val]: 
                        sourceQueue.append(nextNode.val)
        
        for key in indegrees.keys(): 
            if indegrees[key]: 
                return ""
        return ''.join(outputList)