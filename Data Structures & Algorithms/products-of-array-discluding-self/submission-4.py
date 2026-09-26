class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        prefix = [1] * n
        postfix = [1] * n

        prefix[0] = nums[0]
        postfix[n-1] = nums[n-1]

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]

        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        
        output[0] = postfix[1]
        output[n-1] = prefix[n-2]

        for i in range(1, n-1):
            output[i] = prefix[i-1] * postfix[i+1]

        return output

        

# prefix array: 
# prefix[0] = nums[0]
# prefix[i] = prefix[i-1] * nums[i]
# postfix array: 
# postfix[n-1] = nums[n-1]
# postfix[i] = postfix[i+1] * nums[i]

# output[0] = postfix[1]
# output[n-1] = prefix[n-2]
# output[i] = prefix[i-1] * postfix[i+1]