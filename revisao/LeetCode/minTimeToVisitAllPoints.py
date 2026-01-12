class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        total_time = 0

        for i in range(len(points)-1):
            p1 = points[i]
            p2 = points[i + 1]

            dx = abs(p2[0]-p1[0])
            dy = abs(p2[1]-p1[1])

            total_time += max(dx,dy)

        return total_time


# exemplo 

sol = Solution()
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))