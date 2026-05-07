class Solution:#Given an array nums of distinct integers, return all possible permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
	#base cases
        if nums is None:
            return [[]]
        if len(nums) == 1:
            return [nums]

        dp = {} #tried a dp approach, I'll have to come back to this someday because it apparently took quite a while to run

        def recurse(numSub):#recursive function for finding permutations
            if numSub in dp:
                return dp[numSub]
            elif len(numSub) == 2:#for lists with 2 entries, the entries and the reverse ordering of them should give all total perms
                ans = [list(numSub)] + [list(numSub)[::-1]]
                dp.update({numSub: ans})
                return ans
            elif len(numSub) < 2:#if there's just one or less then return the list and move on
                return list(numSub)
            else:
                ans = []
                for i in range(len(numSub)-1, -1, -1):#more complex case where you divide bigger lists up
                    subSub = tuple(numSub[:i] + numSub[i+1:])
                    recAns = recurse(subSub)
                    for j in recAns:
                        ans += [j + [numSub[i]]]
                        print(ans)
                dp.update({numSub: ans})
                return ans
    
        return recurse(tuple(nums))

        