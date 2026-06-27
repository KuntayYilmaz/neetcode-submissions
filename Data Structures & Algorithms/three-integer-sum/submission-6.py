class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashset = []
        output = []

        #Moving tackle
        for tackle in range(len(nums) - 2):
            L, R = tackle + 1, len(nums)-1
            #Start moving Two Pointer
            while R > L:
                 
                current = nums[tackle] + nums[R] + nums[L]
                currentIndexes = [nums,R,L]

                if current > 0:
                    R += -1
                elif current < 0:
                    L += 1
                elif current == 0 and currentIndexes not in hashset and [nums[tackle],nums[R],nums[L]] not in output:
                    output.append([nums[tackle],nums[R],nums[L]])
                    hashset.append(currentIndexes)
                    L += 1
                else:
                    L += 1

        return output

                


                


            
        






        