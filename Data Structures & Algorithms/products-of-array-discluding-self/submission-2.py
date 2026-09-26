class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                output[i] *= nums[j]
        
        return output
                
        



# for index i
# for index j
# if i = j, skip brah
#   compute product of everything
# store in output[i]
# return output

# ts is O(n^2) tho so its hella chopped