class Solution:#Given an integer array, return all triplets that sum to 0. No repeated elements and no duplicate triplets.
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() #Our algorithm later ends up being O(n**2) so an O(nlog(n)) sort to start doesnt kill us much
        #Sorting is the key to making our algorithm work fast
	ans = []
        for i, n in enumerate(nums[:-2]):#Quit when less than 2 elements left
            if i > 0 and n == nums[i - 1]:#If we get a repeat n, skip it
                continue

            l = i + 1
            r = len(nums) - 1

	    #idea here is to do 2sum with n as the "target" and you use left and right pointers to navigate the sorted array
            while l < r:
                sum = n + nums[l] + nums[r]
		#Summing all 3 instead of summing 2 and checking if it equals -n actually saves a ton of time

                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    ans.append([n, nums[l], nums[r]])
                    l += 1
		    #This while loop saves your life and makes it so that duplicates never show up in the summing part
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return ans