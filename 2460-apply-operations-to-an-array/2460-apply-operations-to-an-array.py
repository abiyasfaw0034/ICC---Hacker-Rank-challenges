class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Shift all zeros to the end
        non_zero_idx = 0
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_idx] = nums[i]
                non_zero_idx += 1
        
        while non_zero_idx < n:
            nums[non_zero_idx] = 0
            non_zero_idx += 1
        
        return nums