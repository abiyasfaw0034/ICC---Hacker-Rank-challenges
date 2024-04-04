class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if(nums[right]):
                nums[left],nums[right] = nums[right],nums[left]
                left +=1


# i = 0
        
#         for j in range(len(nums)):
#             if nums[j] != 0:
#                 nums[i] = nums[j]
#                 i += 1
        
#         while i < len(nums):
#             nums[i] = 0
#             i += 1