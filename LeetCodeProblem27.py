class Solution:#for int array nums and int val, remove all occurrances of val in nums in-place. Then return the number of elements in nums that are not equal to val
    def removeElement(self, nums: List[int], val: int) -> int:
        ret = 0
        if not nums:
            return 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i] #python has a delete operation that occurs in-place as far as I can tell, so it's trivial.
            else:
                ret += 1
        return ret

        