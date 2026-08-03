class Solution:#Given array of n integers, return an array of all unique quadruplets that add up to target
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()#as before, sort to make this easier
        ans = []
        stack = []#we use a stack here for the sake of making a recursive function work nicely, but there's other ways to implement this I'm sure

        def kSum(k, start, targ):#We've given up and just made a generic function for summing any k numbers. Thankfully we only have to do 4.
            if k != 2:#All this case really does is ensure every pair of unique numbers get chosen as the non-twosum candidates
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    stack.append(nums[i])
                    kSum(k - 1, i + 1, targ - nums[i])
                    stack.pop()
                return
            if k == 2:#Literally just implement TwoSumII code with some changes (Leetcode 167 I believe)
                l = start
                r = len(nums) - 1

                while l < r:
                    sum = nums[l] + nums[r]

                    if sum < targ:
                        l += 1
                    elif sum > targ:
                        r -= 1
                    else:
                        ans.append(stack + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        
        kSum(4, 0, target)
        return ans