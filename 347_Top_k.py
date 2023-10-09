class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        ans_build = {}
        ans = [[] for i in range(len(nums)+1)]
        for num in nums:
            if ans_build.get(num) is None:
                ans_build[num] = 1
            else:
                ans_build[num] += 1
        
        for key in ans_build.keys():
            ans[ans_build[key]].append(key)

        final_ans = []
        
        for i in range(len(nums), 0, -1):
            if len(ans[i]) != 0:
                final_ans.extend(ans[i])
                k -= len(ans[i])
            if k == 0:
                break
        return final_ans
                
