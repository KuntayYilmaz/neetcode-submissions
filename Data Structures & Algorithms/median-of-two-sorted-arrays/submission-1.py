class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        if len(nums1) > len(nums2):
            A,B = nums2,nums1
        
        l,r = 0,len(A)-1
        n_A,n_B = len(A),len(B)
        while True:
            a = (l+r) // 2
            b = (n_A+n_B) // 2 - a - 2

            Aleft = A[a] if a > -1 else float("-inf")
            Aright = A[a+1] if a+1 < n_A else float("inf")
            Bleft = B[b] if b > -1 else float("-inf")
            Bright = B[b+1] if b+1 < n_B else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (n_A+n_B) % 2:
                    return min(Aright,Bright)
                
                return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            
            if Aleft > Bright:
                r = a-1
            elif Bleft > Aright:
                l = a+1
            
