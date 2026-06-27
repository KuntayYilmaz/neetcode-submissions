class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hashmap = defaultdict(int)
        n = len(strs)

        ans = ""
        for s in strs:
            tmp = ""
            for c in s:
                tmp += c
                hashmap[tmp] += 1
                if hashmap[tmp] == n:
                    ans = tmp
        
        return ans