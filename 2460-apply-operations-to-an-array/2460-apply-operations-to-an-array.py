class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        Left = 0
        for i in range(n):
            if nums[i] != 0:
                nums[Left] = nums[i]
                Left += 1
        
        while Left < n:
            nums[Left] = 0
            Left += 1
        
        return nums