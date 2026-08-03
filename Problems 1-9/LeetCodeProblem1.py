class Solution: #Given array of ints, return indices of two numbers that add up to target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_diffs = {} #dict that stores numbers we see
        for i, n in enumerate(nums):
            diff = target - n #other part of pair

            if diff in dict_diffs:#If pair found, return
                return [i, dict_diffs[diff]]
            else:
                dict_diffs[n] = i
        return None