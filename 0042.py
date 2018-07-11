class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left = 0
        max_right = 0
        p_left = 0
        p_right = len(height) - 1
        res = 0
        while p_left < p_right:
            h_p_left  = height[p_left]
            h_p_right = height[p_right]
            if h_p_left < h_p_right:
                if max_left < h_p_left:
                    max_left = h_p_left
                else:
                    res += max_left - h_p_left
                p_left += 1
            else:
                if max_right < h_p_right:
                    max_right = h_p_right
                else:
                    res += max_right - h_p_right
                p_right -= 1
        return res
                    