#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 19:39:55 2018

@author: lifanhong

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        #exclude no 0
        if nums[0] > 0 or nums[-1] < 0:
            return []
        #find 0
        zero = 0
        for zero in range(len(nums)):
            if nums[zero] < 0:
                continue
            else:
                break
        print(zero)
        for i in range(len(nums)):
            if i > zero:
                break
            j = i + 1
            k = len(nums) - 1
            while k > j:
                if k < zero:
                    break
                if nums[i] + nums[j] + nums[k] > 0:
                    k = k - 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j = j + 1
                else:
                    temp = sorted([nums[i], nums[j], nums[k]])
                    if temp not in output:
                        output.append(temp)
                        #how to remove duplicate in a list of lists
                    k = k - 1
                    j = j + 1
        return output

nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))