class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = [float('inf')] * 26
        finish = [-1] * 26
        n_s = len(s)
        for i in range(n_s):
            char = ord(s[i]) - ord('a')
            if start[char] == float('inf'):
                start[char] = i
                finish[char] = i
            else:
                finish[char] = i

        curr_start = 0
        result = []
        while curr_start < n_s:
            curr_finish = finish[ord(s[curr_start])-ord('a')]
            i = 0
            while i < 26:
                if curr_start < start[i] < curr_finish:
                    curr_finish = max(curr_finish,finish[i])
                    start[i] = float('inf')
                    i = 0
                else:
                    i += 1

            result.append(curr_finish-curr_start+1)
            curr_start = curr_finish+1

        return result

        