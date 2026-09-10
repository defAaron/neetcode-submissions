class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_dict = {}

        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
        
        sorted_nums = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True) #lambda  (helper) function to use second value as sorting value

        return [x[0] for x in sorted_nums[:k]]




# create dictionary nums_dict
# loop through nums
# if num exists in dictionary: value += 1
# else: value = 1
# arrange dictionary so that values are in descending order
# call first k keys of nums_dict        