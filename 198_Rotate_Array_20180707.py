#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 11:45:33 2018

@author: lifanhong

Hackathon AC:
CWC(0/25)
GHX(0/25)
LJQ(0/25)
LFH(4/25)7+13+67+189

"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums += [0 for i in range(k)]
        for j in range(len(nums) -1 , -1 , -1):
            nums[j] = nums[j-k]
        if k != 0:
            del nums[-k:]
        print(nums)

Solution().rotate([1,2,3,4,5,6,7],3)