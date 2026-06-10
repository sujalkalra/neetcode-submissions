class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        parent = [i for i in range(n+1)]
        rank = [0]*(n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            pa,pb =find(a),find(b)
            if pa == pb:
                return  False
            
            if rank[pa] < rank[pb]:
                parent[pa] = pb
            elif rank[pb]<rank[pa]:
                parent[pb] = pa
            else:
                parent[pb] = pa
                rank[pa]+=1
            
            return True
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]