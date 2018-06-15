#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 00:31:26 2018

@author: lifanhong
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.board = [["."] * n] * n
        self.output = []
        self.my_queens(0)
        return self.output
        i = 0

    def my_queens(self, row):
        flag = False
        for i in range(self.n):
            if self.available(row, i):
                self.board[row][i] = 'Q'
                if row == self.n-1:
                    self.output.append([''.join(rows) for rows in self.board])
                    flag = True
                elif self.my_queens(row + 1):
                    flag = True
                self.board[row][i] = '.'#tried out all the solutions when here's a Q
            else:
                continue
        return flag

    
    def available(self, i, j):
        for k in range(i):
            if self.board[k][j] == 'Q':
                return False
        k,l = i - 1,j - 1
        while k >= 0 and l >= 0:
            if self.board[k][l] == 'Q':
                return False
            k,l = k - 1,l - 1
        k,l = i - 1, j + 1
        while k >= 0 and l <= self.n-1:
            if self.board[k][l] == 'Q':
                return False
            k,l = k - 1,l + 1
        return True

print(Solution().solveNQueens(4))