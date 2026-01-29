class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[float('inf')] * 26 for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0 

        for o,c,z in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], z)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue

            u, v = ord(s) - ord('a'), ord(t) - ord('a')
            min_c = dist[u][v]

            
            if min_c == float('inf'):
                return -1
            
            total_cost += min_c

        return int(total_cost)