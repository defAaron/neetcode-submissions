class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checked = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in checked:
                return [checked[diff], i]
            
            else:
                checked[nums[i]] = i



# write a dictionary (checked = {})
# check nums[i] against target
# calculate difference for index i (the new_num needed to achieve target)
# check new_num in dictionary
# if new_num does not exist: 
#   1. store nums[i] and corresponding i in checked{}
#   2. move to next nums[i]
# if new_num exists:
#   return index i and index of new_num


