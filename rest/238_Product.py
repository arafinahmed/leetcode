class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                if zero_count > 1:
                    return [0] * len(nums)
                continue
            prod *= num

        res = []
        for num in nums:
            if num == 0:
                res.append(prod)
            elif zero_count == 1:
                res.append(0)
            else:
                res.append(prod / num)
        
        return res