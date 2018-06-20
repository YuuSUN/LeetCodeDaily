#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 04:42:39 2018

@author: lifanhong
"""
class Solution:    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.output = []
        self.board = [["." for i in range(n) ] for j in range(n) ]
        self.left = [True for i in range(2*n-1)]
        self.right = [True for i in range(2*n-1)]
        self.row = [True for i in range(n)]
        self.solve(0)
        return len(self.output)
    
    def solve(self, n):
        flag = False
        for i in range(self.n):
            if self.checkQ(n,i):
                self.board[n][i] = 'Q'
                self.use(n,i,False)
                if n == self.n - 1:
                    self.output.append([''.join(row) for row in self.board])
                    flag = True
                elif self.solve(n+1):
                    flag = True
                self.board[n][i] = '.'
                self.use(n,i,True)
            else:
                continue
        return flag
    

    def checkQ(self, x, y):
        if self.row[y] == True and self.left[x-y+self.n-1] == True and self.right[x+y] == True:
            return True
        else:
            return False
        
    def use(self, x, y, status):
        self.row[y] = status
        self.left[x-y+self.n-1] = status
        self.right[x+y] = status

print(Solution().solveNQueens(4))