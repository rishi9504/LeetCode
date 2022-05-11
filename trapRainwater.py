# trapRainwater.py

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Intuition: The sum of the water bar height is equal to the sum of the water bar height at each index.
# The water bar height at each index i is determined by the longest bar to the left of the index, l,
# and the longest bar to the right of the index, r. More specifically, the water bar height over
# i is given by min(l, r) - height[i] if height[i] < min(l, r), and 0 otherwise. 
# Therefore, an intuitive solution is to construct two arrays left, and right, where left[i] (right[i]) 
# records the height of the longest bar to the left (right) of i. Finally, we just need to iterate over height,
# and sum over min(l, r) - height[i] at each index if height[i] < min(l, r). The solution is O(n) in time, and O(n) and space.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        highest_right = [0]*len(height)
        for i in range(len(height)-2,-1,-1):
            highest_right[i] = max(highest_right[i+1], height[i+1])
        highest_left,depth = [0]*len(height) , 0
        for i in range(1,len(height)):
            highest_left[i] = max(highest_left[i-1], height[i-1])
            depth+= max(0,min(highest_left[i],highest_right[i])-height[i])
        return depth   


