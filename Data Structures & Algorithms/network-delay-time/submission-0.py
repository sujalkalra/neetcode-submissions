class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        
        dist = {i:float('inf') for i in range(1,n+1)}
        dist[k] = 0

        heap = [(0,k)]

        while heap:
            time,node = heapq.heappop(heap)
            if time >dist[node]:
                continue
            
            for nei,t in graph[node]:
                new_time = time+t
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap,(new_time,nei))
        
        ans = max(dist.values())
        return ans if ans != float('inf') else -1
