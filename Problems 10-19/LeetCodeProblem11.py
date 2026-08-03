class Solution:#For int array representing wall heights, find max area contained by them and x axis
    def maxArea(self, height: List[int]) -> int:

        if not height or len(height) < 2:#easy base cases
            return 0

	#have a left and right pointer that move inward based on which is smaller
	#Important to note that smaller height is what bottlenecks here
        l = 0
        r = len(height) - 1
        temp = 0
        maxArea = (r - l) * min(height[l], height[r])

        while l < r:
            if height[r] <= height[l]:#Move right pointer in if smaller
                temp = height[r]
                r = r - 1
                if height[r] > temp:#Since we're shrinking length, smaller or equal height will never give more area
                    maxArea = max(maxArea, (r - l) * min(height[l], height[r]))
            else:#Move left pointer in if smaller
                temp = height[l]
                l = l + 1
                if height[l] > temp:
                    maxArea = max(maxArea, (r - l) * min(height[l], height[r]))

        return maxArea