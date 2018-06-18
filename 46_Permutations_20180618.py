#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 23:28:53 2018

@author: lifanhong
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.output = []
        self.len = len(nums)
        self.recur(nums)
        no_rep = []
        [no_rep.append(i) for i in self.output if not i in no_rep]
        return no_rep
    
    def recur(self, nums):
        for i in range(len(nums)):
            if len(nums) > 2:
                p_1 = self.recur(nums[:i] + nums[i+1:])
                for j in range(len(p_1)):
                   p_1[j].insert(0, nums[i])
            elif len(nums) == 2:
                p_1 = [nums,[nums[1],nums[0]]]
            else:
                p_1 = [nums]
            if len(nums) == self.len:
                self.output += p_1
        return p_1

print(Solution().permute([1,2,3,4]))