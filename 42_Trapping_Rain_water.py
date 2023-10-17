class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_left, max_right = height[0], height[n - 1]
        left, right = 1, n - 2
        ans = 0

        while left <= right:
            if max_left < max_right:
                if height[left] < max_left:
                    ans += (max_left - height[left])
                else:
                    max_left = height[left]
                left += 1
            else:
                if height[right] < max_right:
                    ans += (max_right - height[right])
                else:
                    max_right = height[right]
                right -= 1
        return ans