# https://leetcode.com/problems/two-sum/

def twoSum(self, nums, target):
        
        indicies = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in indicies:
                return [indicies[complement], i]

            else:
                indicies[num] = i