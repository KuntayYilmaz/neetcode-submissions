class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            tmp = [0] * 26
            for c in s:
                tmp[ord(c) - ord('a')] += 1
            
            hashmap[tuple(tmp)].append(s)
        
        res = []
        for v in hashmap.values():
            res.append(v)
        return res