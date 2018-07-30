#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 19:57:59 2018

@author: lifanhong
"""

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        hist = [0 for i in range(len(matrix[0]))]
        s = 0
        for row in matrix:
            for i,col in enumerate(row):
                if col == '0':
                    hist[i] = 0
                else:
                    hist[i] += 1
            print(hist)
            s = max(s, self.histmax(hist))
        return s
        
    def histmax(self, row):        
        a,b,s = 0,0,0
        while a <= max(row):
            b = 0
            for i in row:
                if i < a:
                    s = max(s, a*b)
                    b = 0
                else:
                    b += 1
#                    print(a,b)
#            print(a,b,s)
            s = max(s, a*b)
            a += 1
        return s

matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

print(Solution().maximalRectangle(matrix))
                
        