from collections import deque
class Solution:
    def bfs(self, adj):
        v=len(adj)
        visited=[False]*v
        queue=deque([0])
        visited[0]=True
        
        bfs_traversal=[]
        
        while queue:
            node=queue.popleft()
            bfs_traversal.append(node)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    queue.append(neighbor)
                    
        return bfs_traversal