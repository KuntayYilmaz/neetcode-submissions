class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        arr = []
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        
        freqSoFar = 0


        for i in range(k):
            for num,freq in hashmap.items():
                if freq > hashmap.get(freqSoFar,0):
                    freqSoFar = num
            arr.append(freqSoFar)
            hashmap.pop(freqSoFar)

        return arr


        
            



        