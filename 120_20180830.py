#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:48:40 2018

@author: lifanhong
"""

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(Solution().minimumTotal())