class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for i in range(len(strs)):
            sorted_str = sorted(strs[i])
            sorted_key = tuple(sorted_str)
            if sorted_key in hashmap:
                hashmap[sorted_key].append(strs[i])
            else:
                hashmap[sorted_key] = [strs[i]]
        
        return hashmap.values()


        