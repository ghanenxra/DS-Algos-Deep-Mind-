class Solution:
    def dfs(self, adj):
        v=len(adj)
        visited=[False]*v
        res=[]
        
        def dfs_traversal(node):
            visited[node]=True
            res.append(node)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs_traversal(neighbor)
                    
            
        dfs_traversal(0)
        return res