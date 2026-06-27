class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        schedulePrio = [(-v,k) for k,v in counter.items()]
        heapq.heapify(schedulePrio)

        schedule = []
        while schedulePrio:
            task = heapq.heappop(schedulePrio)
            for i in range(-task[0]):
                schedule.append((1 + i * (n+1),task[1]))

        heapq.heapify(schedule)
        curr_time = 0

        while schedule:
            task_time,task = heapq.heappop(schedule)

            if task_time <= curr_time:
                task_time = curr_time + 1

            curr_time = task_time

        return curr_time
