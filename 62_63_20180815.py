#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 10:20:54 2018

@author: lifanhong
"""

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[1] * m] + [[1] + [0] * (m-1)] * (n-1)
        for i in range(1,n):
            for j in range(1,m):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[n-1][m-1]
        
        
print(Solution().uniquePaths(7,3))

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        grid = [[1] * m] + [[1] + [0] * (m-1)] * (n-1)
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                elif i == 0 and j == 0:
                    grid[i][j] = 1
                elif i == 0:
                    grid[i][j] = grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i-1][j]
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[n-1][m-1]