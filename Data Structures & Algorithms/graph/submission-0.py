class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        self.graph[src].append(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        if dst not in self.graph[src]:
            return False
        self.graph[src].remove(dst)
        return True
        
    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src, dst, set())

    def dfs(self, node, dst, visited):
        if node == dst:
            return True
        if node in visited:
            return False
        visited.add(node)
        for neighbor in self.graph[node]:
            if self.dfs(neighbor, dst, visited):
                return True
        visited.remove(node)
        return False
        
        

