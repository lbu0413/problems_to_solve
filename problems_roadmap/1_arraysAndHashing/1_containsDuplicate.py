# https://leetcode.com/problems/contains-duplicate/
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# 9-11-2023

def containsDuplicate(nums):
    checker = set()

    for i in nums:
        if i in checker:
            return True
        else:
            checker.add(i)
    
    return False