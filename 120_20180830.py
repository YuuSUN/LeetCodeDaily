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
        self.triangle = triangle
        self.branchmin = dict()
        return self.miniSub(0,0)
        
        
    def miniSub(self,i,j):
        """
        input: position of the tip
        output:minimun of the triangle with tip i,j
        """
        if i == len(self.triangle) - 1:
            return self.triangle[i][j]
        else:
            if (i,j) not in self.branchmin.keys():
                self.branchmin[(i,j)] = min(self.miniSub(i+1,j), self.miniSub(i+1,j+1))
            return self.triangle[i][j] + self.branchmin[(i,j)]
        
        
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(Solution().minimumTotal(triangle))