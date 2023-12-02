class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        
        return list(ans.values())