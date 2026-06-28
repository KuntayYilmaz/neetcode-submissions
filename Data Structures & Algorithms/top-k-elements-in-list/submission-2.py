class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        arr = [[count,num] for num,count in counts.items()]
        arr.sort(reverse=True)

        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans
