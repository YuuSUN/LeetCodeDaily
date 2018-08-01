#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 15:09:09 2018

@author: lifanhong
"""

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.image = image
        oc = image[sr][sc]
        
        if oc == newColor:
            return image
        
        self.dfs(sr,sc,oc,newColor)
        
        return self.image
        
        
    def dfs(self, sr, sc, oc, nc):
        r = len(self.image) - 1
        c = len(self.image[0]) - 1

        if sr < 0 or sc < 0 or sr > r or sc > c or self.image[sr][sc] != oc:
            return
        
        if self.image[sr][sc] == oc:
            self.image[sr][sc] = nc
            self.dfs(sr-1,sc,oc,nc)
            self.dfs(sr,sc-1,oc,nc)
            self.dfs(sr+1,sc,oc,nc)
            self.dfs(sr,sc+1,oc,nc)

        
print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))