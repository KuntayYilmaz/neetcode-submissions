class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [(-v) for k,v in counter.items()]
        heapq.heapify(maxHeap)

        queue = deque()
        curr_time = 0

        while maxHeap or queue:
            if maxHeap:
                curr_task = heapq.heappop(maxHeap)
                curr_time += 1
                if curr_task != -1:
                    queue.append((curr_task+1,curr_time+n))
                if queue and queue[0][1] == curr_time:
                    heapq.heappush(maxHeap,queue.popleft()[0])
            else:
                curr_time += 1
                if queue and queue[0][1] == curr_time:
                    heapq.heappush(maxHeap,queue.popleft()[0])
        
        return curr_time

        

        
