class Solution:#Given an already sorted array of numbers, return 2 unique indices such that they sum to a target. Return the indices + 1 (for 1 indexed array)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:#There was a constraint to not use any fancy data structures so we just do a 2 pointer approach
            sum = numbers[l] + numbers[r]

	    #if sum is too small, increment left, for too big increment right, otherwise we have our answer
            if sum < target:
                l += 1
                while numbers[l] == numbers[l - 1]:
                    l += 1
            elif sum > target:
                r -= 1
                while numbers[r] == numbers[r + 1]:
                    r -= 1
            else:
                return [l + 1, r + 1]
        
        return [None, None]