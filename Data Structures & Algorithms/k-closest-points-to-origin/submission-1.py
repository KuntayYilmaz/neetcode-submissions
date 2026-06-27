class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [[(cord[0]**2 + cord[1]**2) ** 1/2 ,cord] for cord in points]
        heapq.heapify(minHeap)

        out = []
        for i in range(k):
            out.append(heapq.heappop(minHeap)[1])

        return out
        