import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = {}
        count = 0

        for start, end, time in times:
            if start not in edges:
                edges[start] = []
            edges[start].append((time, end))

        
        heap = [(0,k)]
        heapq.heapify(heap)
        visited = set()

        while heap:
            time, cur = heapq.heappop(heap)
            if cur in visited:
                continue
            count += 1
            if count == n:
                return time
            visited.add(cur)
            if cur not in edges:
                continue
            for nexttime, nextnode in edges[cur]:
                heapq.heappush(heap, (time+nexttime, nextnode))
        
        return -1
        