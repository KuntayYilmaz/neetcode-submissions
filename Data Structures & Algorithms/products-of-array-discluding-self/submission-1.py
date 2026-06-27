class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []

        total_product = 1
        zero_count = 0

        for n in nums:
            if n == 0:
                zero_count += 1
                continue
            total_product *= n

        for n in nums:
            if zero_count == 1:
                if n == 0:
                    res.append(total_product)
                else:
                    res.append(0)
            elif zero_count == 0:
                res.append(int(total_product/n))    
            else:
                res.append(0)

        return res

        