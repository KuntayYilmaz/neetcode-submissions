class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [float("-inf") for _ in range(3)]
        prev_match = 0
        for r in range(len(triplets)):
            prev = result
            result = [max(triplets[r][c],result[c]) for c in range(3)]
            n_match = 0
            for c in range(3):
                if result[c] == target[c]:
                    n_match += 1
            if n_match <= prev_match: # nothing changes
                result = prev
            else:
                prev_match = n_match # closer to target
            
        return result == target
                

