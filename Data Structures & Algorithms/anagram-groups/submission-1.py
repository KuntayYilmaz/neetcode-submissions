class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(strs[i])
            else:
                hashmap[sorted_str] = [strs[i]]
        
        return hashmap.values()


        