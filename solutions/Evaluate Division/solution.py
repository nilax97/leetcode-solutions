class Solution:
    def dfs(self, start, comp, w):
        self.w[start] = [comp, w]
        for j, weight in self.edges[start]:
            if self.w[j][0] == -1:
                self.dfs(j, comp, w/weight)
      
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        varbs = set(chain(*equations))
        result, it = [], 0
        self.edges = defaultdict(list)
        for it, [i,j] in enumerate(equations):
            self.edges[i].append([j, values[it]])
            self.edges[j].append([i, 1/values[it]])
            
        self.w = defaultdict(list)
        for var in varbs: self.w[var] = [-1,-1]
            
        for key in varbs:
            if self.w[key][0] == -1:
                self.dfs(key, it, 1)
                it += 1
                
        for a,b in queries:
            if a not in varbs or b not in varbs or self.w[a][0] != self.w[b][0]:
                result.append(-1.0)
            else:
                result.append(self.w[a][1]/self.w[b][1])
                
        return result
        
