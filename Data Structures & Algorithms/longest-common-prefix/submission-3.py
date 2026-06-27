class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = float("inf")
        for s in strs:
            n = min(n,len(s))

        ans = ""
        i = 0
        flag = False
        while(i <= n):
            tmp = strs[0][:i+1]
            for s in strs:
                if s[:i+1] != tmp:
                    flag = True
                    break

            if flag:
                break
            i += 1

        return strs[0][:i]