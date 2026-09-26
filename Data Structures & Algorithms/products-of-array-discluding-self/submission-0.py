class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]

        for i in range(len(nums)):
            for j in range(len(nums)):
                product *= nums[i + 1]
            
            final_product = product / nums[i]

        output[i] = final_product



# looping through every nums[i]:
# calculate product of all nums then divide by nums[i]
# assign product to output[i]