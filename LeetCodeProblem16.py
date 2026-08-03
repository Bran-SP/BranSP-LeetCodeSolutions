class Solution:#Given array of nums and a target find the 3 integers at distinct indices of nums such that the sum is closest to target. Return that closest sum. Assume there is always exactly 1 solution
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()#Sort to make our algorithm work fast
        min = float('inf')
        for i, n in enumerate(nums[:-2]):
            if i > 0 and n == nums[i - 1]:#Skip any used numbers
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:#Basically just implementing structure of normal 3sum
                sum = n + nums[l] + nums[r]

		#small changes below to show we want to save the closest sum value
                if sum < target:
                    if target - sum < abs(min - target):
                        min = sum
                    l += 1
                elif sum > target:
                    if sum - target < abs(min - target):
                        min = sum
                    r -= 1
                else:
                    return target#If we find the exact target then we're done.
        
        return min